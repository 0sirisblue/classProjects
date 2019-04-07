swPkgsPurchased = 0

DISCOUNT_PERC0 = 0
DISCOUNT_PERC10 = 0.1
DISCOUNT_PERC20 = 0.2
DISCOUNT_PERC30 = 0.3
DISCOUNT_PERC40 = 0.4

SOFTPRICE = 99

discountRate = 0

print("Thank you for choosing Software Sales Inc! We offer volume discounts for all software purchases.\n")
print("Your software is available for $99.\nThe following discounted rates apply:\n")
print("10-19 units: 10% discount")
print("20-49 units: 20% discount")
print("50-99 units: 30% discount")
print("100+  units: 40% discount\n")

swPkgsPurchased = int(input("How many software packages would you like to purchase?: "))

if swPkgsPurchased >= 10 and swPkgsPurchased <= 19:
    discountRate = DISCOUNT_PERC10
elif swPkgsPurchased >= 20 and swPkgsPurchased <= 49:
    discountRate = DISCOUNT_PERC20
elif swPkgsPurchased >= 50 and swPkgsPurchased <= 99:
    discountRate = DISCOUNT_PERC30
elif swPkgsPurchased >= 100:
    discountRate = DISCOUNT_PERC40
else:
    discountRate = DISCOUNT_PERC0

initPurchPrice = (swPkgsPurchased * SOFTPRICE)
discountAmt = (swPkgsPurchased * SOFTPRICE * discountRate)
finalPurchase = initPurchPrice - discountAmt

if discountRate != 0:
    print('\nYou have qualified for a discount!')
    print("You saved a total of $" + format(discountAmt, ",.2f") + " on your purchase today!")
    print("Your total purchase comes to $" + format(finalPurchase, ",.2f"))
else:
    print("We're sorry, " + str(swPkgsPurchased) + " units don't qualify for a volume discount.")
    print("Your total purchase comes to $" + format(finalPurchase, ",.2f"))