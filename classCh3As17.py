congratsMsg = "\nGreat, you're online!"
didThatHelpMsg = "Did that solve your connection issues? "

print("We're sorry you're having wireless network issues.\n")
print("We will attempt to solve your connections issues, by walking you through common troubleshooting steps.")
print("Please navigate the following guide by typing 'yes' or 'no' when prompted.\n")

print("First, let's try rebooting your computer.")

usercheck = input(didThatHelpMsg)
if usercheck == "yes":
    print(congratsMsg)
else:
    print ("\nThat's okay.\nLet's try rebooting your router.")
    usercheck = input(didThatHelpMsg)
    if usercheck == "yes":
        print(congratsMsg)
    else:
        print("\nNo problem.\nLet's check that the cables between the router and the modem are snug.")
        usercheck = input(didThatHelpMsg)
        if usercheck == "yes":
            print(congratsMsg)
        else:
            print("\nThat's alright.\nLet's try connecting the router in another location.")
            usercheck = input(didThatHelpMsg)
            if usercheck == "yes":
                print(congratsMsg)
            else:
                print("\nLooks like there's an issue with your router.\nYou should get another one to test with.")