#!/usr/bin/node
const tag = document.querySelector('#red_header');
tag.onclick = addRed;
function addRed () {
  document.querySelector('header').classList.add('red');
}
