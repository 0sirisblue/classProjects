CALS_PER_MIN = 4.2

for minutes in [10, 15, 20, 25, 30]:
    calsBurned = minutes * CALS_PER_MIN
    print("In " + str(minutes) + " minutes you have burned " + str(calsBurned) + " calories.")