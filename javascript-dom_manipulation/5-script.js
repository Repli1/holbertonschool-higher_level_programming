#!/usr/bin/node
const tag = document.querySelector('#update_header');
tag.onclick = changeText;
function changeText () {
  document.querySelector('header').innerHTML = 'New Header!!!';
}
