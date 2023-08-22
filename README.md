# Golf Adventure
[Gold Adventure](xxxxx) is a short version for a round of golf and are played in a python terminal. The player will have to choose between two options on each shot, both choices have different outcome. So the player has to guess which shot will get the ball closer to the hole, to receive the lowest possible score.

---

### How to use    
1. To be able to play the game, you have to click this [link](xxxxx), or copy `https://www.....` and paste into your browser's address bar and press enter.
2. When the page is loaded, click "RUN PROGRAM", and the game will load.
3. Enter your name when told to, use only letters(no whitespaces) and press Enter.
4. Now you'll be taken to the clubhouse, where you can either choose to play game, check out the leaderboard, read the rule book or leave the game. Navigate using your keyboards numbers 1-4 and hit enter.
5. When start a game, your caddie will give you instructions for the hole and which options that are available for the upcoming shot. When told to enter your choice, use your keyboards number and hit enter. The caddie will give you new instructions and options for the next shot. The caddie will do so until the ball is in the hole. You can choose to leave the game at any time, just follow the instructions.
6. When the ball is in the hole, the caddie presents your result and you can choose to submit your score and head back to the clubhouse or you can choose to leave the game without submitting your score. Follow the instructions and use your keyboards numbers and hit enter to make your choice. A Google spreadsheet is automatically collecting your score when submitted.
7. When returning to the clubhouse you can now choose to check out the leaderboard using your keyboards numbers and hit enter. The leaderboard is collecting the top 5 scores from the Google spreadsheet.


---

### User stories
- As a first-time player I want the game to be easy to understand and simple to play. So I've tried my best to explain how it works in the rule book and let the player only use the numeric keyboard instead of mixing it up with letters, except of course when entering the players name.
- For a player that wants to try and get the highscore it's easy to just launch the game again and try another path to shoot a lower score than previous rounds.

---

### Features
- ##### Welcome message.
When starting the game the player will receive a welcome message where the caddie presents himself and the player is asked to enter it's name.
For a better UX I've added green color to the welcome message, using the blessed package.
When entering the player name the player is asked to provide it with only letters, no whitespaces. Or else it will return a Invalid name error and ask the player to give it another try. The error message is red, to make it more obvious that something went wrong.
When the player have entered a valid name it will clear the terminal and thank the player for submitting a name and send them to the "clubhouse".

For UX I've added the time.sleep function to make the letters appear one after each other, I think it makes the text easier for the player to read and follow along.


- ##### Clubhouse.


- ##### Start Game.


- ##### Leaderboard.


- ##### Rule book.


- ##### Leave game.


---

### Flowchart


---

### Technologies used

###### Languages

- [Python](https://www.python.org/): The main language used to develop the application.
- [JavaScript](https://www.javascript.com/): The language used by the Code Institute to run the mock terminal in the browser.
- [HTML](https://www.w3schools.com/html/): The language used by the Code Institute to create the layout needed to run the mock terminal in the browser.

###### Frameworks, libraries, and packages
- [time]
- [blessed]
- [os]
- [sys]


###### Other tools
- [Git]
- [GitHub]
- [CodeAnywhere]
- [Chrome]
- [Draw.io]

---

### Bugs and issues

- ##### Solved bugs


- ##### Unsolved bugs


---

### Testing



#### Manual Testing



###### Validator results


---

### Deployment


---

### Credits

