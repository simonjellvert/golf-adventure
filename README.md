# Golf Adventure
[Gold Adventure](xxxxx) is a short version for a round of golf and are played in a python terminal. The player will have to choose between two options on each shot, both choices have different outcome. So the player has to guess which shot will get the ball closer to the hole, to receive the lowest possible score.

---

### How to use    
1. To be able to play the game, you have to click this [link](xxxxx), or copy `https://www.....` and paste into your browser's address bar and press enter.
2. When the page is loaded, click "RUN PROGRAM", and the game will load.
3. Enter your name when told to, use only letters(no whitespace) and press Enter.
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
When entering the player name the player is asked to provide it with only letters, no whitespace. Or else it will return a Invalid name error and ask the player to give it another try. The error message is red, to make it more obvious that something went wrong.
When the player have entered a valid name it will clear the terminal and thank the player for submitting a name and send them to the "clubhouse".

For UX I've added the time.sleep function to make the letters appear one after each other, I think it makes the text easier for the player to read and follow along.

![Screenshot of welcome message](assets/welcome_page.png)

- ##### Clubhouse.
When entered a valid name on the welcome message, the terminal will clear screen and thank the player for submitting name along with the clubhouse menu options. The welcome message is printed in green along with the inserted name.

In the clubhouse menu the player is given 4 options: either to start the game by entering keyboard number 1 + enter-key, check out the leaderboard by pressing 2 +enter-key, read the rule book of the game by pressing 3+enter-key or leave the game by pressing 4+enter-key.
If the player use an invalid keyboard option a error message will appear in red colored text to make it obvious that something went wrong and the player will have to try again. 
When entering a valid option the terminal is cleared, then printing a message of "Loading leaderboard..." or "Launching game..." etc. Then the terminal is cleared again before showing the players option content.

![Screenshot of clubhouse menu](assets/clubhouse.png)

- ##### Start Game.
Before the game starts a print message is shown as "Launching the game...", then the terminal is cleared before the caddie gives the player instructions about the hole and what options for the first shot the player can choose between.
The player chooses the next shot by using the numeric keyboard and enter-key. On each shot options the player can choose to leave the game. If entering a letter or a symbol an error message will appear in red text telling the player something went wrong and asks to enter option again.

The text is printed using the time.sleep function to make the letters appear one after each other, I think it makes the text easier for the player to read and follow along.

![Screenshot of first shot](assets/play_function.png)

- ##### Next shot.
After choosing a shot, the caddie will present it's outcome followed by instructions for the next shot and it's options. This procedure will continue until the ball is in the hole.
The terminal will clear and show the outcome for this shot, or print a welcome back message if the player chooses to leave the game.

The player chooses the next shot by using the numeric keyboard and enter-key. On each shot options the player can choose to leave the game. If entering a letter or a symbol an error message will appear in red text telling the player something went wrong and asks to enter option again.

The text is printed using the time.sleep function to make the letters appear one after each other, I think it makes the text easier for the player to read and follow along.

![Screenshot of next shot](assets/play_second_shot.png)

- ##### Submit score or leave game.
When the ball is in the hole, the caddie will present the score for the round and ask the player if it wants to submit score and head back to the clubhouse or leave the game without submitting score. The terminal will clear and either load the clubhouse or print a welcome back message, depending on the players choice.

The player chooses it's option using the numeric keyboard and enter-key. If entering a letter or a symbol an error message will appear in red text telling the player something went wrong and asks to enter option again.

The text is printed using the time.sleep function to make the letters appear one after each other, I think it makes the text easier for the player to read and follow along.

![Screenshot of submtting score or leave game](assets/submit_score.png)

- ##### Leaderboard.
In the clubhouse if the player chooses the check out the leaderboard, the terminal will clear and print "Loading leaderboard..." before showing it's content.
The leaderboard is connected to Google spreadsheet using API's and retrieve the top 5 scores with name and score. The score is shown in negative or positive numbers, as they are in the actual game of golf.
The heading on the leaderboard is green colored.

When done with the leaderboard the player is asked to press 1+enter-key to head back to the clubhouse. If entering a invalid choice (letter or symbol) an error message is shown in red colored text, and asks the player to try again.

![Screenshot of leaderboard](assets/leaderboard.png)

- ##### Rule book.
If the player wants to read about the rules of the game it presses 3 on the numeric keyboard + enter-key. 
The rule book is loaded using the file.read() function, because the content of the rule book is stored in a text file on the text_files folder in the workspace.

When done reading the rule book the player is asked to press 1+enter-key to head back to the clubhouse. If entering a invalid choice (letter or symbol) an error message will appear in red colored text, and asks the player to try again.

![Screenshot of rule book](assets/rule_book.png)

- ##### Leave game.
The player can leave the game at any time. There's options for that in the clubhouse and after each shot. The player is informed how to do so and just needs to follow the instructions provided. When they leave the game a welcome back message appears in the terminal.
If the player entered a invalid choice (letter or symbol) an error message will appear in red colored text, and asks the player to try again.

![Screenshot of welcome back message](assets/exit_message.png)

- ##### Invalid choice message.
When the player enters a invalid input, whether it's entering numbers or symbols in the name input, or letters or symbols in the play shot input, they receive a error message, telling the player that something went wrong and asks them to try again.
The error message is red colored to make it obvious for the player.

![Screenshot of error message](assets/invalid_choice.png)

---

### Flowchart
In this flowchart you can see the logic that i tried to apply to the game.

![Screenshot of flowchart](assets/flowchart.png)

---

### Technologies used

###### Languages

- [Python](https://www.python.org/): The main language used to develop the game.
- [JavaScript](https://www.javascript.com/): The language used by the Code Institute to run the mock terminal in the browser.
- [HTML](https://www.w3schools.com/html/): The language used by the Code Institute to create the layout needed to run the mock terminal in the browser.

###### Frameworks, libraries, and packages
- [time](https://docs.python.org/3/library/time.html): Used to add sleep function and UX.
- [blessed](https://pypi.org/project/blessed/): Used to add colors to the text and UX.
- [os](https://docs.python.org/3/library/os.html): Used for clear terminal function.
- [sys](https://docs.python.org/3/library/sys.html): Used for print slow function.


###### Other tools
- [GitHub](https://github.com/): Used to host source code.
- [CodeAnywhere](https://app.codeanywhere.com/): Used to write source code.
- [Chrome](https://www.google.com/chrome/): Used to run game in browser.
- [Lucidchart](https://www.lucidchart.com/): Used for create flowchart.
- [CI Python Linter](https://pep8ci.herokuapp.com/): Used to test code.

---

### Bugs and issues

- ##### Solved bugs
- Update leaderboard function didn't handle int's correctly when returning them to check leaderboard function.
    - Fixed by turning both player name and score to strings.
- Print messages too long for terminal in browser.
    - Fixed by adding new lines where needed.
- 


- ##### Unsolved bugs
No unsolved bugs.

---

### Testing
The game was tested continuously in CA terminal to make sure each function worked as expected. When finishing the structure of the whole code i deployed in Heroku to test it in the browser environment.


#### Manual Testing
| Feature Tested | Expected Outcome | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Welcome message | Welcomes the player and asks for name input | Shows message and asks to enter valid name | Pass |
| Check for valid name | Make sure no numbers or symbols are entered within name | Show error message if entered numbers or symbols | Pass
| Clubhouse - Start game | Shows intro of first hole with options to select shot or exit game | Shows caddie instructions and option to play first shot and exit game | Pass |
| Clubhouse - Leaderboard | Retrieve scores from spreadsheet, narrow down to top 5 and show return to clubhouse option | Shows leaderboard, 5 scores and return to clubhouse option | Pass |
| Clubhouse - Rule book | Read content in txt.file and print to terminal, with option to return to clubhouse | Shows rule book and option to return to clubhouse | Pass |
| Exit game | Show a welcome back message and end script | Shows a welcome back message | Pass |
| Shot functions | Display a comment from caddie: result from previous shot, options for next shot and leave game option | Shows comment from caddie and options for next shot | Pass |
| Check for invalid input when choosing shot | Make sure no letters or symbols are entered | Error message appears when entered letters or symbols or irrelevant numbers | Pass |
| Submit score | Update spreadsheet with entered player name and score from round | Spreadsheet is updated | Pass |
| 


###### Validator results

The code was run through [CI PEP8 online validator](https://pep8ci.herokuapp.com/#) with no warnings or errors.

![Screenshot of CI PEP8 validator]
---

### Deployment


---

### Credits

# Golf Adventure
[Gold Adventure](xxxxx) is a short version for a round of golf and are played in a python terminal. The player will have to choose between two options on each shot, both choices have different outcome. So the player has to guess which shot will get the ball closer to the hole, to receive the lowest possible score.

---

### How to use    
1. To be able to play the game, you have to click this [link](xxxxx), or copy `https://www.....` and paste into your browser's address bar and press enter.
2. When the page is loaded, click "RUN PROGRAM", and the game will load.
3. Enter your name when told to, use only letters(no whitespace) and press Enter.
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
When entering the player name the player is asked to provide it with only letters, no whitespace. Or else it will return a Invalid name error and ask the player to give it another try. The error message is red, to make it more obvious that something went wrong.
When the player have entered a valid name it will clear the terminal and thank the player for submitting a name and send them to the "clubhouse".

For UX I've added the time.sleep function to make the letters appear one after each other, I think it makes the text easier for the player to read and follow along.

![Screenshot of welcome message](assets/welcome_page.png)

- ##### Clubhouse.
When entered a valid name on the welcome message, the terminal will clear screen and thank the player for submitting name along with the clubhouse menu options. The welcome message is printed in green along with the inserted name.

In the clubhouse menu the player is given 4 options: either to start the game by entering keyboard number 1 + enter-key, check out the leaderboard by pressing 2 +enter-key, read the rule book of the game by pressing 3+enter-key or leave the game by pressing 4+enter-key.
If the player use an invalid keyboard option a error message will appear in red colored text to make it obvious that something went wrong and the player will have to try again. 
When entering a valid option the terminal is cleared, then printing a message of "Loading leaderboard..." or "Launching game..." etc. Then the terminal is cleared again before showing the players option content.

![Screenshot of clubhouse menu](assets/clubhouse.png)

- ##### Start Game.
Before the game starts a print message is shown as "Launching the game...", then the terminal is cleared before the caddie gives the player instructions about the hole and what options for the first shot the player can choose between.
The player chooses the next shot by using the numeric keyboard and enter-key. On each shot options the player can choose to leave the game. If entering a letter or a symbol an error message will appear in red text telling the player something went wrong and asks to enter option again.

The text is printed using the time.sleep function to make the letters appear one after each other, I think it makes the text easier for the player to read and follow along.

![Screenshot of first shot](assets/play_function.png)

- ##### Next shot.
After choosing a shot, the caddie will present it's outcome followed by instructions for the next shot and it's options. This procedure will continue until the ball is in the hole.

The player chooses the next shot by using the numeric keyboard and enter-key. On each shot options the player can choose to leave the game. If entering a letter or a symbol an error message will appear in red text telling the player something went wrong and asks to enter option again.

The text is printed using the time.sleep function to make the letters appear one after each other, I think it makes the text easier for the player to read and follow along.

![Screenshot of next shot](assets/play_second_shot.png)

- ##### Submit score or leave game.
When the ball is in the hole, the caddie will present the score for the round and ask the player if it wants to submit score and head back to the clubhouse or leave the game without submitting score. 

The player chooses it's option using the numeric keyboard and enter-key. If entering a letter or a symbol an error message will appear in red text telling the player something went wrong and asks to enter option again.

The text is printed using the time.sleep function to make the letters appear one after each other, I think it makes the text easier for the player to read and follow along.

- ##### Leaderboard.
When the player wants to check the leaderboard the terminal clears and prints "Loading leaderboard...". After that message the leaderboard is loaded

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

