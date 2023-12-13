#!/usr/bin/node
const { argv } = require('process');
const number_of_occ = Number (argv[2]);
if (isNaN(number_of_occ)){
	console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < number_of_occ; i++){
		console.log('C is fun');
	}
}
