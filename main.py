import lists
import random
from timeit import default_timer as timer
from colorama import Fore

######################## Objects and Classes ########################

randAvaliable = random.randint(0, 2315) # Obtains a random number between 0 - 2315 (the length of our array which contains the answer words we use)

word = lists.actualWords[randAvaliable] # Assigns the word variable to a word at the random index in our array of answer words

guessedLetters = [] # Creates an empty array to hold the individual letters in the users current guess

allGuessedLetters = [] # Creates an empty array to hold all the individual letters the user has ever guessed that were in the word

correctLetters = [] # Creates an empty array to hold the letters the user has guessed correctly

totalGuessesArr = [] # Creates an empty array to hold the number of guesses it takes the user each time

everyWord = [] # Creates an empty array to hold the previous words the user has entered

greenLetters = []

yellowLetters = []

possibleLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

######################## Primatives & Strings ########################

currentWord = "" # Initializes the current word to blank (keeps track of what letters the user has entered and stores the word at the end)

hintsLeft = 5 # Stores the number of hints the user has

guessesLeft = 6 # Stores the number of guesses the user has

correct = 0 # Keeps track of whether or not the user has guessed all 5 letters correctly

guessed = False # Keeps track of if the user has guessed the word or not

start = timer() # Starts our timer

######################## Method 1 ########################

def PreviousEntries(word, everyWord):  
  # Loops for each word in our list
  for previousWord in everyWord:
    # Loops 5 times
    for x in range(5):
      print(Fore.WHITE + "", end="") # Sets/Resets the output color of the text to white
      flag = False # Sets/Resets the flag to False

      # Checks to see if the current character of the guess matches the selected word
      if (word[x] == previousWord[x]):
        print(Fore.GREEN + previousWord[x], end="") # Prints the guessed letter in a green color

      # Loops 5 times
      for i in range(5):
        # Checks to see if the guessed letter matches any of the letters in the selected word and makes sure that their indexes don't match
        if (previousWord[x] == word[i] and not(previousWord[x] == word[x])):
          print(Fore.YELLOW + previousWord[x], end="") # Prints the guessed letter in a yellow color
          flag = True # Sets the flag to true (tells the below if-statement to run)   
          break

      # Checks to make sure that the guessed word's letter at position x doesn't match the selected word's letter at the same position, also makes sure that the guessed word's letter isn't anywhere in the selected word
      if (not(previousWord[x] == word[x]) and flag == False):
        print(previousWord[x], end="") # Prints the guessed word's letter as is (no color)

    print(Fore.WHITE + "", end="") # Resets the output color of the text to white
    print()

######################## Method 2 ########################

def Wordle():
  # Gives our function access to all of our inialized variables
  global randAvaliable
  global word
  global guessedLetters
  global allGuessedLetters
  global guessesLeft
  global correct
  global guessed
  global end
  global correctLetters
  global everyWord
  global currentWord
  global greenLetters
  global yellowLetters

  # Runs our Wordle "program" so long as there are guesses left and the user hasn't guessed the word yet
  while (guessesLeft > 0 and guessed == False):
    guess = input("Enter a guess: ") # Prompts the user for their first guess

    # Makes sure that the word entered is in one of our lists and is exactly 5 letters
    while (not(guess in lists.guessableWords or guess in lists.actualWords) or (len(guess) > 5 or len(guess) < 5)):
      if (guess == "Hint" or guess == "hint"):
        guess = Hint(guess) # If guess equals hint then call the Hint method
        
      elif(len(guess) > 5 or len(guess) < 5):
        print()
        guess = input("Incorrect input, please enter 5 letters: ")
        
      else:
        print()
        guess = input("Not a word, try again: ")

    # Loops through the user's guessed word and adds the individual characters to an array
    for letter in guess:
      guessedLetters.append(letter)
  
    print()

    # Loops 5 times
    for x in range(5):
      print(Fore.WHITE + "", end="") # Sets/Resets the output color of the text to white
      flag = False # Sets/Resets the flag to False

      # Checks to see if the current character of the guess matches the selected word
      if (guessedLetters[x] == word[x]):
        print(Fore.GREEN + guessedLetters[x], end="") # Prints the guessed letter in a green color
        correct = correct + 1 # Adds 1 to the number of correct letters

        allGuessedLetters.append(word[x]) # Adds the current letter to the array which stores all the letters the user has ever guessed that were in the word

        greenLetters.append(word[x])

        currentWord = currentWord  + word[x] # Adds the letter to the current word

        # If the word at the current index is not already in our correctLetters array it is added 
        if (not(word[x] in correctLetters)):
          correctLetters.append(word[x])

      # Loops 5 times
      for i in range(5):
        # Checks to see if the guessed letter matches any of the letters in the selected word and makes sure that their indexes don't match
        if (guessedLetters[x] == word[i] and not(guessedLetters[x] == word[x])):
          print(Fore.YELLOW + guessedLetters[x], end="") # Prints the guessed letter in a yellow color
          
          flag = True  # Sets the flag to true (lets the bottom if-statement know to run as the letter guessed doesn't exist anywhere in the word)
          
          allGuessedLetters.append(guessedLetters[x]) # Adds the current letter to the array which stores all the letters the user has ever guessed that were in the word

          yellowLetters.append(guessedLetters[x])
          
          currentWord = currentWord + guessedLetters[x] # Adds the letter to the current word 

          break

      # Checks to make sure that the guessed word's letter at position x doesn't match the selected word's letter at the same position, also makes sure that the guessed word's letter isn't anywhere in the selected word
      if (not(guessedLetters[x] == word[x]) and flag == False):
        print(guessedLetters[x], end="")  # Prints the guessed word's letter as is (no color)

        currentWord = currentWord + guessedLetters[x] # Adds the letter to the current word 

        # Checks to see if the letter is avaliable to be removed from the array of possible letters
        if (guessedLetters[x] in possibleLetters):
          possibleLetters.remove(guessedLetters[x])
          
    print(Fore.WHITE + "", end="") # Resets the output color of the text to white

    guessesLeft = guessesLeft - 1  # Removes one from the number of guesses
    
    print()
    print()

    everyWord.append(currentWord)  # Adds the guessed word to the array which stores all the words
    currentWord = "" # Resets the guessed word

    # If the last guessed word got all 5 letters correct
    if (correct == 5):
      print("That's correct!")
  
      guessed = True

      end = timer() # Ends the timer

      Stats() # Calls our Stats method
    
      break

    # Checks to make sure that the user has guesses left
    if (guessesLeft > 0):
      print("You have " + str(guessesLeft) + " guesses left.") # Tells the user how many guesses they have left

      print()

      print("------------------------------------------------------------")

      print()

      print("Previous guesses: ")
      PreviousEntries(word, everyWord) # Calls our first method to list all the previously entered words

      print()

      print("Potential letters: ")

      # Loops through and prints all the letters that could possibly be in the word
      for letter in possibleLetters:
        if (letter in greenLetters):
          print(Fore.GREEN + letter + " ", end="")
        elif (letter in yellowLetters):
          print(Fore.YELLOW + letter + " ", end="")
        else:
          print(Fore.WHITE + letter + " ", end="")

      print()    
      print()

    # If the user is out of guesses then it lets them know and prints out the selected word
    else:
      print("You ran out of guesses!")

      print()
      
      print("The word was: " + word)

      end = timer() # Ends the timer

      Stats() # Calls the Stats method
    
      print()

    guessedLetters.clear() # Clears the array of guessed letters for the next guess

    correct = 0 # Resets the number of correct letters for the next guess

######################## Method 3 ########################

def Hint(guess):
  # Accepts the choosen word and hintsLeft declared at the start of the program
  global word, allGuessedLetters, hintsLeft

  print(allGuessedLetters)
  
  counter = 0

  # While the guess entered is Hint or hint
  while (guess == "Hint" or guess == "hint"):
    print()

    # If there are still hints remaining
    if (hintsLeft > 0):
      randLetter = random.randint(0, 4) # Get a random integer between 0 and 4
      hint = word[randLetter] # Set the hint equal to the letter at that random index in the word

      # While that random letter is a part of the array of letters that the user already knows are in the word
      while (hint in allGuessedLetters):
        # Get a new random letter that is in the word
        randLetter = random.randint(0, 4)
        hint = word[randLetter]

        counter = counter + 1 # Add one to the counter

        # If this while loop runs more than 200 times (almost certainly means that there are no letters that the user already doesn't know)
        if (counter > 200):
          hintsLeft = 0 # Manually sets the number of hints left to 0
          break # Ends our while loop

      # If there are hints left
      if (hintsLeft > 0):
        allGuessedLetters.append(hint) # Add to the array of the letters the user has guessed the letter from the hint
        
    # Checks if there are no hints left
    if (hintsLeft == 0):
      print("There are no Hints left to give")
      
      print()
      
      guess = input("Enter a guess: ")
      
    else:
      print("The letter " + hint + " is in the word.")
      
      hintsLeft = hintsLeft - 1
      
      print()
      
      guess = input("Enter a guess: ")
      
  return guess

######################## Method 4 ########################

def Stats():
  global end
  global start
  global hintsLeft
  global guessesLeft
  global correctLetters
  global totalGuessesArr

  numCorrect = 0

  totalGuesses = 0

  avgGuesses = 0

  count = 0

  # For each letter the user has guessed correctly by the end (either got the word or used up all the guesses) add one to the number of letters they guessed correctly
  for letter in correctLetters:
    numCorrect = numCorrect + 1

  print()
  print("Stats:")
  
  totalTime = end - start # Obtains the time taken
  totalTime = round(totalTime, 2) # Rounds that time to 2 decimal places
  print("Time: " + str(totalTime) + " seconds")

  score = ((10000 / totalTime) * (guessesLeft + 1) * numCorrect) - (5000 * (5 - hintsLeft)) # Calculates the users score

  # Checks to see if the users score is below 0 (if so sets it to 0)
  if (score < 0):
    score = 0
  
  score = round(score) # Rounds the score to an integer
  print("Score: " + str(score))

  totalGuessesArr.append(6 - guessesLeft) # Adds the number of guesses it took to the arrary which keeps stores the number of guesses it took each individual time

  # For each individual piece of data in the number of guesses array
  for x in totalGuessesArr:
    totalGuesses = totalGuesses + x # Add all those numbers up
    count = count + 1 # Calculate the number of them

  avgGuesses = totalGuesses / count # Get the average number of guesses it takes the user to guess the word

  print("Average Guesses: " + str(avgGuesses))


######################## Setup ########################
Wordle()
  
# Loops 50 times
for x in range(50):
  print()
  
  play = input("Play again? (Y or N): ")

  # Checks to see if the user wants to play again
  if (play == "Y" or play == "y" or play == "yes"):
    print()

    # Resets all the original variables
    randAvaliable = random.randint(0, 2315)
    word = lists.actualWords[randAvaliable]
        
    guessedLetters.clear()
    allGuessedLetters.clear()
    greenLetters.clear()
    yellowLetters.clear()
    
    guessesLeft = 6
    hintsLeft = 5
    correct = 0
    everyWord.clear()
    
    guessed = False

    possibleLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    Wordle()
  else:
    break