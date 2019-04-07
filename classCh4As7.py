payRate = 0.01
totalPay = 0.00

numDays = int(input("How many days will you be employed?: "))

print("Daily Salary\tTotal Pay")
print("--------------------------")

for day in range(0, numDays):
    totalPay = totalPay + payRate
    print(format(payRate, '.2f') + "\t \t " + format(totalPay, '.2f'))
    payRate = payRate * 2
