# Wordle Python
## Description
Replica of the game Wordle I built in high school for the APCSP final project and my first real coding project. Although I am sure it is familiar to many, objective of the game is to guess the hidden five-letter word within 6 attempts. Users can request hints and try as many words as they want. Statistics describing the users' preformance will be printed out upon end of game.


## How to Play
You can download this github project onto your own device and run the program in a terminal.</br>
```
# command to run the project
python main.py
# you may also need to install the following libraries
pip install lists random timeit colorama
```

## Walkthrough
Program begins by prompting user to enter a guess. Invalid words that are too long, too short, or not a word, will result in repromting. After entering a valid 5 letter word, the word will be reprinted with color-coded markings. Yellow ~ the letter is in the word but in the wrong place, green ~ the letter is in the right place, and white ~ the letter is not in the word. Below this, the program will update and print your remaining number of guesses.</br>
<img width="484" alt="Screenshot 2024-09-19 at 8 26 46 PM" src="https://github.com/user-attachments/assets/5a160b35-ccea-41db-ac61-7b55c4e478aa">
For the next guess, a line will be printed to distinguish between the two. Above the enter prompt, previous guesses will be printed in order, alongside a list of potential letters. Removed from this list will be letters already determined not to be in the word, while yellow and green letters will be highlighted.</br>
<img width="504" alt="Screenshot 2024-09-19 at 8 30 31 PM" src="https://github.com/user-attachments/assets/05f652b1-7a09-4209-aa04-002292d94745">
Instead of a guess users may enter "hint" to get a hint on a letter that is in the word and has not yet been found. If all letters have been found then no hint will be given.</br>
<img width="233" alt="Screenshot 2024-09-19 at 8 38 23 PM" src="https://github.com/user-attachments/assets/cb624f74-53fd-48d9-84fa-37826915212d">
Upon guessing the word, the user will be congratulated and their preformance stats (time, score, average guesses) will be printed. Resulting score is based upon the number of guesses, number of hints, number of correct letters, and time.</br>
<img width="295" alt="Screenshot 2024-09-19 at 8 51 57 PM" src="https://github.com/user-attachments/assets/6aefe32c-271a-4b74-aeb1-08a919b1c964">
If you fail to guess the word, the game will end and the word will be revealed to the user along with their stats.
<img width="242" alt="Screenshot 2024-09-19 at 8 44 36 PM" src="https://github.com/user-attachments/assets/51606614-9862-45eb-9811-9e54899c8840">
At the end of the program you will have the option to continue.</br>
<img width="205" alt="Screenshot 2024-09-19 at 8 52 32 PM" src="https://github.com/user-attachments/assets/019691d5-1274-4fb7-aa7b-c4f786fa54ea">
