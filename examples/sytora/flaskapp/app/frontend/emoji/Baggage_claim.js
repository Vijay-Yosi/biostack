import React from 'react';

export default function Baggage_claim(props) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" enableBackground="new 0 0 64 64" width={64} height={64} {...props}>
      <circle cx={32} cy={32} r={30} fill="#4fd1d9" />
      <g fill="#fff">
        <circle cx="14.5" cy={48} r={2} />
        <circle cx="21.5" cy={48} r={2} />
        <circle cx="28.5" cy={48} r={2} />
        <circle cx="35.5" cy={48} r={2} />
        <circle cx="42.5" cy={48} r={2} />
        <circle cx="49.5" cy={48} r={2} />
        <path d="m41 19h-2v-3.9c0-.6-.4-1-1-1h-12c-.6 0-1 .5-1 1v3.9h-2v-3.9c0-1.7 1.3-3.1 3-3.1h12c1.7 0 3 1.4 3 3.1v3.9" />
        <path d="m50 19h-3.5v24h3.5c1.1 0 2-.9 2-2v-20c0-1.1-.9-2-2-2" />
        <path d="m19.5 19h25v24h-25z" />
        <path d="m17.5 19h-3.5c-1.1 0-2 .9-2 2v20c0 1.1.9 2 2 2h3.5v-24" />
      </g>
    </svg>
  );
}
