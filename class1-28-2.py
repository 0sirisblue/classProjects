batchCupsSugar = 1.5
batchCupsButter = 1.0
batchCupsFlour = 2.75
batchCookieNum = 48

perCookieSugar = batchCupsSugar / batchCookieNum
perCookieButter = batchCupsButter / batchCookieNum
perCookieFlour = batchCupsFlour / batchCookieNum

desiredCookies = input(int("How many cookies would you like to make?"))

print("You have chosen to make " + str(desiredCookies) + " cookies!")
print("You will need the following ingredients:")
print(str(desiredCookies * perCookieFlour) + " cups of flour")
print(str(desiredCookies * perCookieButter) + " cups of butter")
print(str(desiredCookies * perCookieSugar) + " cups of sugar")