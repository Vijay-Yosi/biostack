import React from 'react';

export default function Womens(props) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" enableBackground="new 0 0 64 64" width={64} height={64} {...props}>
      <circle cx={32} cy={32} r={30} fill="#ff5a79" />
      <g fill="#fff">
        <path d="m36 23h-4-4c-1 0-2 1-2 2l-3 11h3l2-9v4l-2 9h2v11h3v-11h2v11h3v-11h2l-2-9v-4l2 9h3l-3-11c0-1-1-2-2-2" />
        <path d="m36 19c0 1-1 2-2 2h-4c-1 0-2-1-2-2v-4c0-1 1-2 2-2h4c1 0 2 1 2 2v4" />
      </g>
    </svg>
  );
}
