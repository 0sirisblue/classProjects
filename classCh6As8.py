def main():
    numberFileRead = open('randomNumbers.txt', 'r')

    numCounter = 0

    number = numFileRead.readline()

    while number != '':
        number = number.rstrip('\n')
        print(number)
        numberInt = int(number)
        total += numberInt
        numCounter += 1
        number = numberFileRead.readline()

    print("This file contains " str(numCounter) + " numbers, totalling " + str(total))

main()