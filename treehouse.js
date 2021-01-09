// function sayGreeting(greeting = 'Good morning', name = 'student') {
//     return `${greeting}, ${name}!`;
// }


// function getRandomNumber(upper) {
//     return Math.floor( Math.random() * upper ) + 1;
// }

// let counter = 0;

// while ( counter < 10 ) {
//     console.log( `The random number is ${getRandomNumber(10)}`);
//     counter += 1;
// }


// do {
//     console.log( `The random number is ${getRandomNumber(10)}`);
//     counter += 1;
// } while ( counter < 10 );


// for ( let i = 0; i < 10; i++) {
//     console.log( `The random number is ${getRandomNumber(10)}` );
// }


// const main = document.querySelector('main');
// let html = '';

// for ( let i = 0; i < 10; i++ ) {
//     html += `<div>${i}</div>`;
// }

// main.innerHTML = html;

// ----------------------------------------------------------------

// let html = '';
// let red;
// let green;
// let blue;
// let randomRGB;

// red = Math.floor(Math.random () * 256);
// green = Math.floor(Math.random () * 256);
// blue = Math.floor(Math.random () * 256);
// randomRGB = `rgb( ${red}, ${green}, ${blue})`;
// html += `<div style="background=color: ${randomRGB}">${i}</div>`;

// document.querySelector('main').innerHTML = html;

// ----------------------------------------------------------------

// let html = '';
// const randomValue = () => Math.floor(Math.random() * 256);

// function randomRGB() {
//     const color = `rgb( ${randomValue()}, ${randomValue()}, ${randomValue()} )`;
//     return color;
// }

// for ( let i = 1; i <= 10; i++ ) {
//     html += `<div style="background-color: ${randomRGB()}">${i}</div>`;
// }

// document.querySelector('main').innerHTML = html;

// ----------------------------------------------------------------

// let html = '';
// const randomValue = () => Math.floor(Math.random() * 256);

// function randomRGB(value) {
//     const color = `rgb( ${value()}, ${value()}, ${value()} )`;
//     return color;
// }

// for ( let i = 1; i <= 10; i++ ) {
//     html += `<div style="background-color: ${randomRGB(randomValue)}">${i}</div>`;
// }

// document.querySelector('main').innerHTML = html;

// ----------------------------------------------------------------

// const planets = [
//     'Mercury',
//     'Venus',
//     'Earth',
//     'Mars'
// ];

// console.log( planets[0]);

// ----------------------------------------------------------------

// const instruments = ['piano', 'drums', 'trumpet'];
// instruments.push('guitar','violin', 'triangle');
// instruments.unshift('bass');
// instruments.pop('triangle');

// ----------------------------------------------------------------

// const middle = ['lettuce', 'cheese', 'patty'];
// const burger = ['top bun', ...middle, 'bottom bun']

// const brass = ['trumpet', 'trombone', 'french horn', 'baritone', 'tuba'];
// const woodwind = ['flute', 'oboe', 'clarinet', 'saxophone', 'bassoon'];
// const instruments = [...brass, ...woodwind]; 

// console.log(instruments);

// ----------------------------------------------------------------

// const students = ['Lee', 'Jan', 'Mali', 'Sariah'];
//     for ( let i = 0; i < students.length; i++) {
//         console.log ( students[i]);
//     }

// ----------------------------------------------------------------

// const playlist = [
//     'So What',
//     'Respect',
//     'What a Wonderful World',
//     'At Last',
//     'Three Little Birds',
//     'The Way You Look Tonight'
// ];

// function createListItems(arr) {
//     let items = '';
//     for ( let i = 0; i < arr.length; i++ ) {
//         items += `<li>${ arr[i] }</li>`;
//     } return items;
// }

// document.querySelector('main').innerHTML = `
//     <ol>
//         ${createListItems(playlist)}
//     </ol>
// `;

// ----------------------------------------------------------------

// const daysInWeek = [
//     'Monday',
//     'Tuesday',
//     'Wednesday',
//     'Thursday',
//     'Friday',
//     'Saturday',
//     'Sunday'
// ]

// console.log( daysInWeek.join(', '); )
// console.log( daysInWeek.includes('Friday'); )
// console.log( daysInWeek.indexOf('Wednesday'); )

// ----------------------------------------------------------------

// const inStock = [
//     'pizza', 'cookies', 'eggs', 'apples', 'milk', 'cheese', 'bread', 'lettuce', 'carrots', 'broccoli',
//     'potatoes', 'crackers', 'onions', 'tofu', 'limes', 'cucumbers'];

// const search = prompt('Search for a product.');
// let message;

// if ( !search ) {
//     message = `<strong>In stock:</strong> ${inStock.join(', ')}`;
// } else if ( inStock.includes(search.toLowerCase) ) {
//     message = `Yes, we have <strong>${search}</strong>.  It's #${inStock.indexOf(search.toLowerCase) + 1} on the list!`;
// } else {
//     message = `Sorry, we do not have <strong>${search}</strong>.`;
// }

// document.querySelector('main').innerHTML = `<p>${message}</p>`;

// ----------------------------------------------------------------

// const playlist = [
//     ['So What', 'Miles Davis', '9:04'],
//     ['Respect', 'Aretha Franklin', '2:45'],
//     ['What a Wonderful World', 'Louis Armstrong', '2:21'],
//     ['At Last', 'Ella Fitzgerald', '4:18'],
//     ['Three Little Birds', 'Bob Marley and the Wailers', '3:01'],
//     ['The Way You Look Tonight', 'Frank Sinatra', '3:21'],
// ];

// // const myArtists = `${playlist[0][1]}, ${playlist[1][1]}, ${playlist[5][1]}`;
// // console.log(myArtists);

// function createListItems(arr) {
//     let items = '';
//     for ( let i = 0; i < arr.length; i++ ) {
//         items += `<li>${ arr[i][0] }, by ${ arr[i][1] } - ${ arr[i][2] }</li>`;
//     } 
//     return items;
// }

// document.querySelector('main').innerHTML = `
//     <ol>
//         ${createListItems(playlist)}
//     </ol>
// `;

// ----------------------------------------------------------------

// const student = { 
//     name: "Quincy",
//     grades: [85, 90, 95, 100]
// };

// const person = {
//     name: "Edward",
//     city: "New York",
//     age: 37,
//     isStudent: true,
//     skills: ["JavaScript", "HTML", "CSS"]
// };

// const message = `Hi, I'm ${ person.name }.  I live in ${ person.city }. 
// Most know me as ${ person.nickname = "Duke" }. My age is ${ person.age + 1}.  
// I have ${ person.skills.length} skills. ${ person.skills.join(', ')}`;
// console.log(message);

// ----------------------------------------------------------------

// const person = {
//         name: "Edward",
//         nickname: "Duke",
//         city: "New York",
//         age: 37,
//         isStudent: true,
//         skills: ["JavaScript", "HTML", "CSS"]
//     };

// for ( let prop in person ) {
//     console.log(`${prop}: ${person[prop]}`);
// }

// ----------------------------------------------------------------

// const questions = [
//     { question: "How many planets are in the Solar System?", answer: "8" },
//     { question: "How many continents are there?", answer: "7" },
//     { question: "How many legs does an insect have?", answer: "6" },
//     { question: "What year was JavaScript created?", answer: "1995" },
// ]

// const correct = [];
// const incorrect = [];
// let correctAnswers = 0;


// for ( let i = 0; i < questions.length; i++ ) {
//     let question = questions[i].question;
//     let answer = questions[i].answer;
//     let response = prompt(question);

//     if ( response === answer ) {
//         correctAnswers++;
//         correct.push(question);
//     } else {
//         incorrect.push(question);
//     }
// }

// ----------------------------------------------------------------

const pets = [
    {
      name: 'Joey',
      type: 'Dog',
      breed: 'Australian Shepherd',
      age: 8,
      photo: 'img/aussie.jpg'
    },
    { 
      name: 'Patches',
      type: 'Cat',
      breed: 'Domestic Shorthair',
      age: 1,
      photo: 'img/tabby.jpg'
    },
    { 
      name: 'Pugsley',
      type: 'Dog',
      breed: 'Pug',
      age: 6,
      photo: 'img/pug.jpg'
    },
    { 
      name: 'Simba',
      type: 'Cat',
      breed: 'Persian',
      age: 5,
      photo: 'img/persian.jpg'
    },
    { 
      name: 'Comet',
      type: 'Dog',
      breed: 'Golden Retriever',
      age: 3,
      photo: 'img/golden.jpg'
    }
  ];

  let html= '';

  for ( let i = 0; i < pets.length; i++) {
      let pet = pets[i];
      html += `
        <h2>${pet.name}</h2>
        <h3>${pet.type} | ${pet.breed}</h3>
        <p>Age: ${pet.age}</p>
        <img src="${pet.photo}" alt="${pet.breed}">
    `;
  }

  document.querySelector('main').insertAdjacentHTML('beforeend', html);

// ----------------------------------------------------------------

