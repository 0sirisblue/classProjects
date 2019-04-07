import random

def main():
    num = 0
    numberFile = open('randomNumbers.txt', 'w')

    print("This program will generate a list of random numbers, and output them to a file.\n")
    numVariables = int(input("How many numbers would you like to generate? "))

    while num < numVariables:
        randomNum = random.randint(1, 500)
        numberFile.write(str(randomNum) + '\n')
        num += 1

    numberFile.close()
    print("Your " + str(numVariables) + " numbers have been written to the file.")

main()