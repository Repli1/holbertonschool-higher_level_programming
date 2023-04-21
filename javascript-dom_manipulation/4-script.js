#!/usr/bin/node
const tag = document.querySelector('#add_item');
tag.onclick = addElem;
function addElem () {
  const node = document.createElement('li');
  const textnode = document.createTextNode('Item');
  node.appendChild(textnode);
  document.getElementsByClassName('my_list')[0].appendChild(node);
}
