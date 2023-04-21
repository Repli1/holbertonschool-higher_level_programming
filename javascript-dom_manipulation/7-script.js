#!/usr/bin/node
const tag = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

async function logJSONData () {
  const response = await fetch(url);
  const data = await response.json();
  for (let i = 0; data.results[i] !== undefined; i++) {
    const node = document.createElement('li');
    const item = data.results[i].title;
    const textnode = document.createTextNode(item);
    node.appendChild(textnode);
    tag.appendChild(node);
  }
}
logJSONData();
