def main():
    
    total = 0
    avgCounter = 0

    try:
        numFile = open('numbers.txt', 'r')
    except IOError:
        print('This file cannot be opened.')

    try:
        number = numFile.readline()
    except ValueError:
        print('This value cannot be read.')
    
    while number != '':
        try:
            numberInt = int(number)
        except ValueError:
            print('This string cannot be converted to an integer.')
        total += numberInt
        avgCounter += 1
        number = numFile.readline()

    average = total / avgCounter

    print("The average of the numbers in your file is: " + str(average))

    numFile.close()

main()