principalAmount = float(input("What was the amount of your initial deposit? "))
interestRateAnnual = int(input("What is your interest rate in percent? "))
compoundTimesAnnual = int(input("How many times a year is your interest compounded? "))
yearsElapsed = int(inp("How many years have elapsed since you made the initial deposit? "))
totalAmount = principalAmount * ( (1+(interestRateAnnual / compoundTimesAnnual)) **  (compoundTimesAnnual * yearsElapsed) )

print("You now have a total of " + str(format(totalAmount, '.2f')))