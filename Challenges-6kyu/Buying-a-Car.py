def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    # Return values: Months, MoneyLeft

    PriceNew = float(startPriceNew)
    PriceOld = float(startPriceOld)
    Money = float(0)
    count = 0
    totalMoney = float(Money + PriceOld)

    while PriceNew > totalMoney:
        # calculate loss per month
        count += 1
        if count % 2 == 0:
            percentLossByMonth += 0.5

        # calculate the price of both cars
        PriceNew = PriceNew - (PriceNew * (percentLossByMonth / 100.0))
        PriceOld = PriceOld - (PriceOld * (percentLossByMonth / 100.0))

        # add savings to pocket
        Money += savingperMonth

        totalMoney = Money + PriceOld

    return [count, int(round((totalMoney - PriceNew), 0))]


print(nbMonths(2000, 8000, 1000, 1.5))
