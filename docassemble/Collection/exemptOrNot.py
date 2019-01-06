def all_income_combined(jobs, non_job_income):
    all_income = list()
    for item in non_job_income:
        all_income.append(item)
    for item in jobs:
        all_income.append(item)
    return all_income

def amount_not_exempt(IncomeList):
    total = float(0)
    for item in IncomeList:
        if item.name in ['Unemployment', 'Social Security', 'Public Assistance (Food Stamps, Cash Assistance)', 'EAEDC', 'Food Stamps', 'Veterans Benefits', 'Pension/Annuity/Retirement']:
            total = total
        else:
            total = total + float(item.amount(period_to_use=52))
    if (float(total) <= 600) is False:
        if ((float(total) * .85) > 600) is True:
            amount_not_exempt = (float(total) * .15)
        else:
            amount_not_exempt = (float(total) - 600)
    else:
        amount_not_exempt = float(0)
    return amount_not_exempt





