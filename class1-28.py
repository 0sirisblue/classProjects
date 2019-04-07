initPurchase = float(input('Please enter your purchase price: '))
SALESTAX_STATE = 0.05
salesTaxStatePer = SALESTAX_STATE * 100
SALESTAX_COUNTY = 0.025
salesTaxCountyPer = SALESTAX_COUNTY * 100
totalPurchase = initPurchase + (initPurchase * SALESTAX_STATE) + (initPurchase * SALESTAX_COUNTY)

print("Your purchase before tax was $" + str(initPurchase) + ".")
print("Your state's sales tax is " + str(salesTaxStatePer) + "%")
print("Your county's sales tax is " + str(salesTaxCountyPer) + "%")
print("Your total purchase price is $" + str(format(totalPurchase, '.2f')) + ".")
