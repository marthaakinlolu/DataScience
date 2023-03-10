# Welcome to My Mastermind
***

## Task
The problem being solved in this program is a code-breaking game, where the player has to guess a 4-digit secret code. 

The code consists of the numbers 0 to 8, with no repetition. The player has 10 rounds to guess the code, and after each round, the player is informed about how many digits are well placed and how many are missplaced.

The challenge of this program is to keep track of the rounds and to determine whether the player's guess is valid or not. 

The program must also randomly generate the secret code if it is not provided as an argument.

## Description
The problem is solved by using several functions, such as miss_counts, well_counts, checkValue, and read_Value. 

The miss_counts and well_counts functions are used to calculate the number of well-placed and missplaced digits in the player's guess. 

The checkValue function is used to validate the player's input. The read_Value function is used to read the player's guess.

## Installation
To install this project, you need to compile the code using a C compiler. 

This can be done by using the gcc command. Once you have compiled the code, you can run the executable file. 

This project does not use npm install or make as it is a C program, not a Node.js or Makefile project.
## Usage
The program works by first generating a secret code if it is not provided as an argument. 

The player then enters a guess in each round, and the program validates the player's input. 

If the input is valid, the program calculates the number of well-placed and missplaced digits and displays the result. If the player successfully guesses the code within 10 rounds, the program congratulates the player.

```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
