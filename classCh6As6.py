def main():
    
    numFile = open('numbers.txt', 'r')

    total = 0
    avgCounter = 0

    number = numFile.readline()
    
    while number != '':
        numberInt = int(number)
        total += numberInt
        avgCounter += 1
        number = numFile.readline()

    average = total / avgCounter

    print("The average of the numbers in your file is: " + str(average))

    numFile.close()

main()