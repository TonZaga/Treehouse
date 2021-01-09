const maxRange = 10;
const maxGuesses = 3;
let currentGuess = 1;

let randomNumber = Math.floor(Math.random() * maxRange + 1);
console.log("The random number is :", randomNumber);

let playerGuess = prompt(`Hi, I've chosen a random number between 1 and ${maxRange}. You have ${maxGuesses} tries to guess it.\n`);

function handleGuess(userGuess){
  for(let guesses = 0; guesses < maxGuesses; guesses++);

    if(userGuess == randomNumber){
      console.log('You win!')
      console.log(
        `You guessed correctly in ${currentGuess} ${
          currentGuess === 1 ? 'try' : 'tries'
        }.`
      );
      guesses = maxGuesses
      playAgain();
    } else if(guesses == maxGuesses - 1){
      console.log('You lose!');
      console.log(`The correct number was ${randomNumber}`);
    } else if(userGuess > randomNumber){
      console.log('Think lower...');
      currentGuess++
      userGuess = prompt('Guess again...');
    } else {
      console.log('Think higher...');
      currentGuess++
      userGuess = prompt('Guess again...');
    }
      
  }

const playAgain = () => {
  let playAgainPrompt = prompt('Do you want to play again? y || n\n\n');
  playAgainPrompt = playAgainPrompt.toLowerCase();
  if(playAgainPrompt === 'y'){
    randomNumber = Math.floor(Math.random() * maxRange + 1);
    console.log("The random number is :", randomNumber);
    currentGuess = 1;
    guesses = 0;
    playerGuess = prompt.question(`Hi, I've chosen a random number between 1 and ${maxRange}. You have ${maxGuesses} tries to guess it.\n`);
    handleGuess(playerGuess);
  }else {
    console.log('See ya, Nerd!');
  }
}

handleGuess(playerGuess);