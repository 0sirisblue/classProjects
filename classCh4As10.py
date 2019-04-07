tuition = 8000

for count in range(5):
    tuition = tuition * 1.03
    print("Year " + str(count + 1) + " tuition will be $" + format(tuition, ',.2f'))