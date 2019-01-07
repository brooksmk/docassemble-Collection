def jobs_and_fully_exempt_combined(jobs, non_job_income):
    jobs_and_fully_exempt = list()
    for item in non_job_income:
        if item.name in ['Workers Compensation', 'Unemployment', 'Social Security', 'Public Assistance (Food Stamps, Cash Assistance)', 'EAEDC', 'Food Stamps', 'Veterans Benefits', 'Pension/Annuity/Retirement']:
            jobs_and_fully_exempt.append(item)
    for item in jobs:
        jobs_and_fully_exempt.append(item)
    return jobs_and_fully_exempt

def fully_non_exempt(non_job_income):
    fully_non_exempt = list()
    total = float(0)
    for item in non_job_income:
        if item.name not in ['Workers Compensation', 'Unemployment', 'Social Security', 'Public Assistance (Food Stamps, Cash Assistance)', 'EAEDC', 'Food Stamps', 'Veterans Benefits', 'Pension/Annuity/Retirement']:
            fully_non_exempt.append(item)
    for item in fully_non_exempt:
        total = total + float(item.amount(period_to_use=52))
    return total

def amount_not_exempt(IncomeList):
    total = float(0)
    for item in IncomeList:
        if item.name in ['Workers Compensation', 'Unemployment', 'Social Security', 'Public Assistance (Food Stamps, Cash Assistance)', 'EAEDC', 'Food Stamps', 'Veterans Benefits', 'Pension/Annuity/Retirement']:
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





