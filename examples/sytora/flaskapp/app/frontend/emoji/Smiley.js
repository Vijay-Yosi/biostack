import React from 'react';

export default function Smiley(props) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" enableBackground="new 0 0 64 64" width={64} height={64} {...props}>
      <circle cx={32} cy={32} r={30} fill="#ffdd67" />
      <g fill="#664e27">
        <circle cx="20.5" cy="24.5" r={5} />
        <circle cx="43.5" cy="24.5" r={5} />
        <path d="m49 38c0-.8-.5-1.8-1.8-2.1-3.5-.7-8.6-1.3-15.2-1.3-6.6 0-11.7.7-15.2 1.3-1.3.3-1.8 1.3-1.8 2.1 0 7.3 5.6 14.6 17 14.6 11.4 0 17-7.3 17-14.6" />
      </g>
      <path d="m44.7 38.3c-2.2-.4-6.8-1-12.7-1-5.9 0-10.5.6-12.7 1-1.3.2-1.4.7-1.3 1.5.1.4.1 1 .3 1.6.1.6.3.9 1.3.8 1.9-.2 23-.2 24.9 0 1 .1 1.1-.2 1.3-.8.1-.6.2-1.1.3-1.6 0-.8-.1-1.3-1.4-1.5" fill="#fff" />
    </svg>
  );
}
