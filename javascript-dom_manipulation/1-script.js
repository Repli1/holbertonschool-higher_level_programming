#!/usr/bin/node
const tag = document.querySelector('#red_header');
tag.onclick = turnRed;
function turnRed () {
  document.querySelector('header').style.color = 'red';
}
