# treasureHunter
A game of treasure hunting in which two players search for buried treasure
while trying to avoid traps and pitfalls.  

# Rules
* The game board is covered in dirt.  Both Treasures and Traps are buried.
* If a player encounters a trap, 50 points are deducted from their health.  
* For every treasure a player finds, a point is added to the score.  
* The game continues until one of the players run out of health at which point the game board will change to white and display a game over message.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 treasureHunter

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- treasureHunter      (source code for game)
  +--data               (data files for message display)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
  +--constants.py       (constant declarations for the program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
* Adam Dutson quibly@byui.edu
* Christopher Infante inf20001@byui.edu
* TJ Miller mil14029@byui.edu


