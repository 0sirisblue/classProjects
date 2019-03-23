# Please name the .py files for your program as M#_Midterm. For example: M08_Midterm.py (Python will 
# automatically append the extensions.  You'll submit this file for grading.
# Your assignment is to write a program that inputs a sentence from the keyboard, word by word, into a list.  
# The program should output the following. 1. Complete Programming Exercise #13 Magic 8 Ball on Page 405-406 of your book
# 8_ball_responses.txt  This assignment asks you to output text responses randomly from a file, and allow it to loop
# until the user chooses to stop



# importing random for a random number, time for a delay
import random
import time

responses = []

#setup opens and reads 8 ball file (runs in and sets up for main)

def setup(): 

    responseFile = open('8_ball_responses.txt', 'r')

    line = responseFile.readline()

    while line != '':
        cleanLine = line.rstrip('\n')
        responses.append(cleanLine)
        line = responseFile.readline()

    responseFile.close()

def main():

#prepping

    setup()

    magicCounter = 0
    magicLen = 0

    guessAgain = 'y'

    print("Welcome to Britton's Magic Py-Ball!!\n\n")

    userQuestionList = []

#giving the user choice

    while guessAgain == 'y' or guessAgain == 'Y':
        userQuestion = input("What is your question for the Magic Py-Ball?\n")
        userQuestionList = userQuestion.split()

        print("\nInteresting question! Let's see...\n")

        time.sleep(2)

        print('Thinking...\n')

        time.sleep(2)

# to generate a random response (reflecting user input yet one based on the "hands of fate" meaning a cryptic interaction)
# ... i'm going to make a special number, combining a small random number from the computer added to two numbers
# based entirely on user input. the first, uses the number of total characters of the users question,
# the second takes the length of the user's input that's been stripped and put into list form.
        
        handsOfFate = random.randint(0,7)

        for ch in userQuestion:
            magicCounter += 1

        magicLen = len(userQuestionList)

# numbers are summed, then ran through a modulo division using a divisor equal to the total number of 8 ball responses

        magicNumber = handsOfFate + magicCounter + magicLen

        responseMagicNum = magicNumber % 12

# print the 8_ball txt response that corresponds to the number we generated

        print("The Magic Py-Ball says...  " + responses[responseMagicNum] + '\n')

        time.sleep(1)

        print("Would you like to ask the Magic Py-Ball another question?\n")
        guessAgain = input("Type 'y' to ask again: ")
        print('\n')

    print("As you wish... farewell!")

main()
