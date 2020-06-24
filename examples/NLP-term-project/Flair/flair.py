
# For creating of the Flair Embeddings
import flair
from flair.data import Corpus
from flair.datasets import ColumnCorpus

columns = {0: 'text', 1: 'pos', 3: 'ner'}

# this is the folder in which train, test and dev files reside
data_folder = './'

# init a corpus using column format, data folder and the names of the train, dev and test files
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='conll_train.txt',
                              test_file='conll_test.txt',
                              dev_file='conll_dev.txt')
tag_type = 'ner'
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

from flair.embeddings import TokenEmbeddings, WordEmbeddings, StackedEmbeddings, PooledFlairEmbeddings, ELMoEmbeddings
from typing import List
embedding_types: List[TokenEmbeddings] = [
    PooledFlairEmbeddings('en-forward'),
    PooledFlairEmbeddings('en-backward'),
]
embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger(hidden_size=256,
                                        embeddings=embeddings,
                                        tag_dictionary=tag_dictionary,
                                        tag_type=tag_type,
                                        use_crf=True)
EMBEDDING_DIMENSION=256


# def balance(data):
#     for j in range(len(data)):
#         X=data[j][0]
#         y=data[j][1]
#         cnt=min([len([i for i in range(len(y)) if y[i]=="O"]),
#                 sum([i=="I-Disease" for i in y]),sum([])])
from flair.trainers import ModelTrainer

trainer: ModelTrainer = ModelTrainer(tagger, corpus)
#  start training
trainer.train('flairmodels/v1',
              learning_rate=0.1,
              mini_batch_size=1,
              max_epochs=10)


