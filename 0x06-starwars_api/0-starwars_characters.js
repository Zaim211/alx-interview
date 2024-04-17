#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
let people = [];
const names = [];

const filmsEndpoint = async () => {
  await new Promise(resolve => request(url, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const responseBody = JSON.parse(body);
      people = responseBody.characters;
      resolve();
    }
  }));
};

const getNames = async () => {
  if (people.length > 0) {
    for (const i of people) {
      await new Promise(resolve => request(i, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const responseBody = JSON.parse(body);
          names.push(responseBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: No Characters found');
  }
};

const responseCharNames = async () => {
  await filmsEndpoint();
  await getNames();

  for (const name of names) {
    if (name === names[names.length - 1]) {
      process.stdout.write(name);
    } else {
      process.stdout.write(name + '\n');
    }
  }
};

responseCharNames();
