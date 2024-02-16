#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log(`Usage: node 0-starwars_characters.js ${movieId}`);
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('API requeset failed with status:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  try {
    for (const characterUrl of characters) {
      const characterBody = await getRequest(characterUrl);
      const character = JSON.parse(characterBody);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
});

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}
