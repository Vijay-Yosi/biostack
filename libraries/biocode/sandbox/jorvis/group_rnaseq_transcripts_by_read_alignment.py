#!/usr/bin/env python3

"""

This script was created after doing RNA-Seq assemblies for the Aplysia project, in which we
had many reference transcripts generated by other means that we attempted to query within
the assembled transcript set, with varying levels of success.  There were many instances
where the transcripts were fragmented quite a lot compared with the reference (and these were
PCR-validated in our source material.)

We wanted another strategy of grouping these transcripts together in the absence of a reference
genome, so this is an attempt to do so using alignment of the source reads back onto the Trinity-
assembled transcripts using tophat2.  Specifically, this script parses the resulting
'accepted_hits.sam' file and looks for mate pairs spanning different contigs.

Reminder: SAM format:
1   QNAME   String     [!-?A-~]{1,255} Query template NAME
2   FLAG    Int        [0,216-1] bitwise FLAG
3   RNAME   String     \*|[!-()+-<>-~][!-~]* Reference sequence NAME
4   POS     Int        [0,231-1] 1-based leftmost mapping POSition
5   MAPQ    Int        [0,28-1] MAPping Quality
6   CIGAR   String     \*|([0-9]+[MIDNSHPX=])+ CIGAR string
7   RNEXT   String     \*|=|[!-()+-<>-~][!-~]* Ref. name of the mate/next read (* unavailable) (= same)
8   PNEXT   Int        [0,231-1] Position of the mate/next read
9   TLEN    Int        [-231+1,231-1] observed Template LENgth
10  SEQ     String     \*|[A-Za-z=.]+ segment SEQuence
11  QUAL    String     [!-~]+ ASCII of Phred-scaled base QUALity+33

WARNING:
There are a lot of conventions for read naming with regard to direction.  Here in the SAM any
of the following are common:

  HWI-D00688:13:C6F54ANXX:7:2111:15500:46809
  HWI-D00688:13:C6F54ANXX:7:2111:15500:46809/1
  HWI-D00688:13:C6F54ANXX:7:2111:15500:46809__1

It's only the base that we care about here, so if the read IDs end with /N or __N those parts will
be stripped.


NOTES:

Tophat2 does put reciprocals in the output file (columns 1,3,7):

  HWI-D00688:13:C6F54ANXX:7:2111:15500:46809__2	c100009_g1_i1	c78654_g1_i1
  HWI-D00688:13:C6F54ANXX:7:2111:15500:46809__1	c78654_g1_i1	c100009_g1_i1


TO ADD:

1.  Include count of total input reads
2.  
  
  
"""

import argparse
from itertools import repeat
import os
import re
import sys
#import pypy (not ready for py3.4 yet)


def main():
    parser = argparse.ArgumentParser( description='Groups transcripts by mapped read pairs')

    ## output file to be written
    parser.add_argument('-i', '--input_sam_file', type=str, required=True, help='SAM file of read alignments back to transcripts' )
    parser.add_argument('-mmpc', '--min_mate_pair_count', type=int, required=True, help='Number of mate pairs spanning two fragments required to group them together.' )
    parser.add_argument('-o', '--output_file', type=str, required=True, help='Output file will have information on transcript groupings' )
    args = parser.parse_args()

    ## describes the pairings between two contigs.  $contig_1 should always sort alphabetically before $contig_2
    #   data[$contig_1][$contig_2] = list($read_bases_pairing_them)
    pairings = dict()
    pairings_over_threshold = 0
    single_read_pairings = 0

    print("INFO: parsing SAM file and creating transcript pairings")

    for line in open(args.input_sam_file):
        if line[0] == '@': continue
        
        cols = line.split("\t")
        ref_read = cols[0]
        ref_transcript = cols[2]
        other_transcript = cols[6]

        # we don't care about the lines where the mate is unmapped or mapped to the same
        if other_transcript == '*':
            single_read_pairings += 1
            continue
        elif other_transcript == '=':
            continue

        m = re.match("(.+)__[12]$", ref_read)
        if m:
            ref_read_base = m.group(1)
        else:
            m = re.match("(.+)\/[12]$", ref_read)
            if m:
                ref_read_base = m.group(1)
            else:
                ref_read_base = ref_read

        transcripts = sorted([ref_transcript, other_transcript])

        rstart = cols[3]
        cigar = cols[5]

        # query
        qstart = 1
        m = re.match("^(\d+)[SH]", cigar)
        if m:
            qstart += int(m.group(1))

        qlen = 0
        for m in re.finditer("(\d+)[M=XI]", cigar):
            qlen += int(m.group(1))

        qend = qstart + qlen - 1

        # reference
        rstart = int(cols[3])
        rlen = 0
        for m in re.finditer("(\d+)[M=XDN]", cigar):
            rlen += int(m.group(1))

        rend = rstart + rlen - 1
        

        if transcripts[0] not in pairings:
            pairings[transcripts[0]] = dict()
            
        if transcripts[1] not in pairings[transcripts[0]]:
            pairings[transcripts[0]][transcripts[1]] = list()

        if ref_read_base not in pairings[transcripts[0]][transcripts[1]]:
            pairings[transcripts[0]][transcripts[1]].append( {
                'id': ref_read_base, 'qstart':qstart, 'qend':qend, 'rstart':rstart, 'rend':rend
            } )
            
            #print("DEBUG: t1:{0} t2:{1} rend:{2}, qstart:{3}, qend:{4}, rstart:{5}, rend:{6}".format(transcripts[0], transcripts[1],
            #    ref_read_base, qstart, qend, rstart, rend
            #))

    print("INFO: Creating transitive groups based on successful pairings")

    # Create transitive groupings based on the successful pairings.
    # Each element here is a list of transcripts in that group
    groups = list()
    
    for transcript1 in pairings:
        for transcript2 in pairings[transcript1]:

            print("DEBUG: Check transcript {0} vs {1}, which has {2} bridges".format(transcript1, transcript2, len(pairings[transcript1][transcript2])))
            if len(pairings[transcript1][transcript2]) >= args.min_mate_pair_count and meets_coverage(pairings[transcript1][transcript2]):
                pairings_over_threshold += 1

                group_found = False
                for group in groups:
                    if transcript1 in group:
                        group_found = True
                        if transcript2 not in group:
                            group.append(transcript2)

                if group_found == False:
                    groups.append( [transcript1, transcript2] )
                    

    print("INFO: There were {0} single-read mappings unused".format(single_read_pairings))
    print("INFO: There were {0} transcript pairings over the min mate pair threshold ({1})".format(pairings_over_threshold, args.min_mate_pair_count))
    print("INFO: These were collapsed into {0} transitive groups".format(len(groups)))

    ofh = open(args.output_file, 'wt')
    
    for group in groups:
        ofh.write("\t".join(group))
        ofh.write("\n")


def meets_coverage(pairings):
    min_bp_coverage = 250
    max_transcript_size = 40000

    # non of our transcripts are over 40k
    qcovered = list(repeat(0,max_transcript_size))

    for pair in pairings:
        for i in range(pair['rstart'] - 1, pair['rend']):
            qcovered[i] = 1

        print("DEBUG:\tqstart:{0}\tqend:{1}\trstart:{2}\trend:{3}".format(pair['qstart'], pair['qend'], pair['rstart'], pair['rend']))
        print("DEBUG:qcovered now: {0}".format(qcovered.count(1)))

    qbases_covered = qcovered.count(1)
    print("DEBUG:\t{0} bases covered".format(qbases_covered))

    if qbases_covered > min_bp_coverage:
        return True
    else:
        return False

if __name__ == '__main__':
    main()







