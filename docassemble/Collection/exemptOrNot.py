def amount_not_exempt(IncomeList):
    total = 0
    for item in IncomeList:
        total = total + item.amount(period_to_use=52)
    if (float(total) <= 550) is False:
        if ((float(total) * .85) > 550) is True:
            return (float(total) * .15)
        else:
            return (float(total) - 550)
    else:
        return 0





