#!/usr/bin/node
const tag = document.querySelector('#toggle_header');
const header = document.querySelector('header');
tag.onclick = toggleColor;
function toggleColor () {
  header.classList.toggle('red');
  header.classList.toggle('green');
}
