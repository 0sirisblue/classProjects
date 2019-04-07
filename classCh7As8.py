girlNamesFile = open('girlnames.txt', 'r')
boyNamesFile = open('boynames.txt', 'r')

girlNames = girlNamesFile.readlines()
boyNames = boyNamesFile.readlines()

girlNamesFile.close()
boyNamesFile.close()

index = 0

while index < len(girlNames):
    girlNames[index] = girlNames[index].rstrip('\n')
    index += 1

index = 0

while index < len(boyNames):
    boyNames[index] = boyNames[index].rstrip('\n')
    index += 1

print("Would you like to search for a Girls's name?\n")

searchedGirlName = input("Type the name or 'n' to skip:")

if searchedGirlName != 'n':
    if searchedGirlName in girlNames:
        print("That name is a popular name for girls!\n")
    else:
        print("That's an unique name.\n")
else:
    print("That's okay. Next question\n")

print("Would you like to search for a Boy's name?\n")

searchedBoyName = input("Type the name or 'n' to skip:")

if searchedBoyName != 'n':
    if searchedBoyName in boyNames:
        print("That name is a popular name for boys!\n")
    else:
        print("That's an unique name.\n")






