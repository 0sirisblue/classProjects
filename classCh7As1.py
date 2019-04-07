def main():
    dailySales = []

    dayOfWeek = 0

    salesTotal = 0

    index = 0

    while dayOfWeek < 7:
        sales = int(input('Please enter the daily sales total in dollars: '))
        dailySales.append(sales)
        dayOfWeek += 1

    while index < len(dailySales):
        salesTotal += dailySales[index]
        index += 1

    print("Your total sales for the week were $" + str(salesTotal))

main()