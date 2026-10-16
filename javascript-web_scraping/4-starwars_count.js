#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    const count = films.filter((film) =>
      film.characters.some((character) => character.endsWith('/18/'))
    ).length;
    console.log(count);
  }
});
