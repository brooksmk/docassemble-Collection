def fully_exempt(income_list):
    for item in income_list:
        if item.amount is <= 550:
            item.amount.exempt = True
        if item.amount is > 550:
            item.amount.exempt = False
    return item.amount.exempt

def amount_not_exempt(income_list):
    for item in income_list:
        if item.amount.exempt = False:
            if item.amount * .15 is > 550:
                item.amount.amount_not_exempt = item.amount * .15
            else:
                item.amount.amount_not_exempt = item.amount - 550
        else:
            item.amount.amount_not_exempt = 0
    return item.amount.amount_not_exempt





