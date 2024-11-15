import time
import random

def main(answers): #basic menu that the player retruns to each game.
    print ("Welcome to Hangman!")
    time.sleep(1)
    print("Would you like to,")
    print("1 - Play a new game")
    print("2 - View the scores")
    print("3 - Exit the program")
    
    start = input("1/2/3:")
    time.sleep(1)
    
    if start == "1":
        print("\n")
        print ("Starting Game...")
        wordgen(answers)
        main(answers)
    
    if start == "2":
        print("\n")
        print ("Printing Scoreboard...")
        printboard()
        main(answers)
        
    if start == "3":
        exit()

    else:
        print("\n")
        print ("Sorry, I didnt understand that answer") #basic if/else statement to prevent the user from causing input errors.
        print("\n")
        time.sleep(1)
        main(answers)

def wordgen(answers):
    attempts = 10
    correct = False #win condition
    print ("You have 10 attempts to guess the correct word!")
    
    answer = random.choice(answers) #choose a random answer from the answers array and cast it to uppercase.
    answer = answer.upper()
    
    letter_list = []
    letter_list[:0] = answer #converts answer string into a list.
    answer_length = len(letter_list)
    hidden_answer = "#" * answer_length #creates a hidden version of the answer in the form of a string.
    time.sleep(1)
    print ("Here is your word:")
    print("\n")
    print (hidden_answer)
    time.sleep(1)
    gameloop(hidden_answer,letter_list,answer,attempts,correct)

def gameloop(hidden_answer,letter_list,answer,attempts,correct):

    while attempts != 0 and correct != True: #while loop that runs list comprehension for each game turn until the player wins or loses.
   
        print("\n")
        print ("Guess a letter!")
        letter = input (">")
        letter = letter.upper()
        time.sleep(1)

        if len(letter) == len(answer): #data validation for entering full word guesses.
            if letter != answer:
                print ("Unlucky! Try again!")
                attempts = attempts - 1 #remove attempts unless the player wins the game that round.
                print ("Turns left:")
                print (attempts)
            if letter == answer: #check if the list has been fully deciphered by the player.
                print ("You guessed right!")
                correct = True
                print ("\n")
                print ("You Win!")
        
        if len(letter) == 1 and letter != "#": #data validation for entering individual characters
            if letter not in answer:
                print ("Unlucky! Try again!")
                attempts = attempts - 1 
                print ("Turns left:")
                print (attempts)

            else:
                print ("You guessed right!")
                answer_list =[]
                answer_list[:0] = hidden_answer #converts "hidden_answer" into a list in a new seperate variable
                
                letter_check = [i for i, item in enumerate(answer) if item == letter] #enumerates the answer strings letters and finds the index of the strings letter that matches the players input"

                for i in letter_check:
                    answer_list[i] = letter #replaces 'answer_list' underscores with correct letter string entered by the player (based on the matching index).
                    
                hidden_answer = "".join(answer_list)#coverts the list into a string for better player readability.
                
                print ("\n")
                print (hidden_answer) #Display the list to the player, so they know how close they are to winning.
                print ("\n")

                if hidden_answer == answer: 
                    correct = True
                    print ("\n")
                    print ("You Win!")

                else:
                    attempts = attempts - 1 
                    print ("Turns left:")
                    print (attempts)

    if attempts == 0:
        print ("You Lose!")
        print ("The word was " + answer )
    
    time.sleep(1)
    print("\n")
    print("#########")
    print("GAME OVER")
    print("#########")
    print("\n")

    if correct == True:
        export(attempts,correct) #if the player wins they can enter thier score into the txt file.
    else:
        main(answers)


def export(attempts,correct):
    score = str(attempts)
    if attempts != 0:
        print ("You finished with " + score + " attempts remaining!")

    time.sleep(1)
    print ("Please enter your name")
    name = input (">")
    name = str(name)

    with open('scores.txt', 'a') as x:
        x.write("\n")
        x.write("// PLAYER: " + name + " // SCORE: " + score + " //") #basic formatting for a txt file leaderboard (CSV would be better).

    print ("Score Saved!")
    main(answers)



def printboard():

    with open('scores.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            
            
    print ("\n")
    time.sleep(1)
    main(answers)


answers = [
    "mausoleum",
    "halo",
    "health",
    "alien",
    "xenomorphic",
    "ethereal",
    "significant",
    "disturbed",
    "mandatory",
    "examination",
    "neolithic",
    "byzantium",
    ]

main(answers)
