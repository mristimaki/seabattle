# Sea Battle
Sea Battle is a Python terminal game that runs in the Code Institute mock terminal on Heroku.
<br>
User is playing the game alone and are to hit all the ships that has randomly been set to the board. Each battleship occupies one square on the board.
<br>
<br>
[Here you can find the live version of the project.](https://seabattle-mristimaki.herokuapp.com/)
<br>

## How to play Sea Battle!

Sea Battle is based on a simple battleship game, in this version the player enters their name and the computer will generate a board that has set three ships randomly to the game. 
<br>
The player will then have total of 10 guesses to hit all the ships before game is over. The player gets to choose a row and a column for each turn to guess.
<br>

## Features
### Existing Features

<img width="742" alt="seabattle_intro" src="https://user-images.githubusercontent.com/121927123/234624904-24818f05-9779-45e1-b13c-2ee5538d4879.png">

- Random bord generation
  - The ships are randomly placed on the board
- One player game
- Accepts user input

<img width="745" alt="check_input" src="https://user-images.githubusercontent.com/121927123/234624514-9105f05c-4282-480a-8f70-e59a69c3612d.png">

- Input validation
  - You cannot enter coordinates that has already been guessed
  - You cannot enter coordinates outside of the size of the grid
  
 <img width="745" alt="game_over" src="https://user-images.githubusercontent.com/121927123/234625097-f3511f2b-997d-4344-8d7c-4666032cbafe.png">

  
### Future Features
- Player against the computer (two boards)
- Letting the player know how many scores they had when game is over.

## Data Model
I have a Battleship class as my model. This class sets the size of the board, the number of ships and details such as player's name.

## Testing
I have manually tested this my project by:
- Passed the code trough a PEP8 linter and confirmed that there are no errors
- Tested in my local terminal and in the Code Institute Heroku terminal
- Used print to debug any problems that I have met along the way

### Bugs
**Solved Bugs**
- My while loop to check if the player has reached the total amount of turns was not working correctly, I fixed it by putting the `turns += 1´ at the end of the while loop instead. 

### Remaining Bugs
- No remaining bugs

### Validator testing
- PEP8
  - No errors returned from https://pep8ci.herokuapp.com/
 
 ## Deployment
 This project was deployed using Code Institute's mock terminal for Heroku.
 <br>
 <br>
 **Steps for deployment are as follows:**
 - Fork or clone this repositry
 - Create a new Heroku app
 - Set the buildpacks to `Python´ and `NodeJS´ in that particular order
 - Link the Heroku app to the repository
 - Click on **Deploy**
 
 ## Credits
 - Code Institute for the deployment terminal
 - A huge thanks to the tutors on Code Institute that has helped me so much with guiding me in the right direction for this project. Especially Holly and Martin that has helped me debug and find solutions to how I could generate the random ships to the board as well as the checking if the total turns has been met. Long hours and a lot of debugging that has helped me!
 - Also a huge thanks to my husband and my two little toddlers that bares with a sleep deprived wife and mother during times of endless studys both day and night.
 
