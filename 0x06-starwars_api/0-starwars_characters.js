#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

let people = [];
const names = [];

const FilmsEndpoint = async () => {
  await new Promise((resolve) => request(url, (err, res, body) => {
    if (err || res.statusCode != 200) {
      console.log('Error: ', err, 'StatusCode: ', res.statusCode);
    } else {
      const jsonResponse = JSON.parse(body);
      people = jsonResponse.characters;
      resolve();
    }
  }));
};

const GetNames = async () => {
  if (people.length > 0) {
    for (const i of people) {
      await new Promise((resolve) => request(i, (err, res, body) => {
        if (err || res.statusCode != 200) {
          console.log('Error: ', err, 'StatusCode: ', res.statusCode);
        } else {
          const jsonResponse = JSON.parse(body);
	  names.push(jsonResponse.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: no Characters found');
  }
};

const ResponseCharNames = async () => {
  await FilmsEndpoint();
  await GetNames();
  for (const name of names) {
    if (name === names[names.length - 1]) {
      process.stdout.write(name);
    } else {
      process.stdout.write(name + '\n');
    }
  }
};

ResponseCharNames();
