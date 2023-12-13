#!/usr/bin/node
class Person {
  name = 'no name';
  constructor (name) {
    this.name = name;
  }

  introduceSelf () {
    console.log(`Hi I'm ${this.name}`);
  }
}

const person = new Person('Pius');
const person1 = new Person();
console.log(person.name);
console.log(person1.name);
