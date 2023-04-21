#!/usr/bin/node
const tag = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

async function logJSONData () {
  const response = await fetch(url);
  const data = await response.json();
  tag.innerHTML = data.name;
}

logJSONData();
