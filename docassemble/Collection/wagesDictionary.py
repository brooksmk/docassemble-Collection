Income = {
    'Source 1': {'Exempt': False, 'Amount': 800, 'Period': 'bi-weekly'},
    'Source 2': {'Exempt': True, 'Amount': 700, 'Period': 'weekly'},
    'Source 3': {'Exempt': False, 'Amount': 14, 'Period': 'hourly'},
    'Source 4': {'Exempt': False, 'Amount': 200, 'Period': 'daily'}
    }

for k in Income:

    if Income[k]['Period'] == 'annual':
        Income[k]['Amount'] = int(Income[k]['Amount'] / 52)
        Income[k]['Period'] = 'weekly'
        
    if Income[k]['Period'] == 'monthly':
        Income[k]['Amount'] = int(Income[k]['Amount'] / 4.3)
        Income[k]['Period'] = 'weekly'
        
    if Income[k]['Period'] == 'bi-weekly':
        Income[k]['Amount'] = int(Income[k]['Amount'] / 2)
        Income[k]['Period'] = 'weekly'
        
    if Income[k]['Period'] == 'weekly':
        Income[k]['Amount'] = Income[k]['Amount']

    if Income[k]['Period'] == 'daily':
        print('How many days per week do you work at ' + str(k) + '?')
        days_per_week = input()
        Income[k]['Amount'] = int(Income[k]['Amount'] * int(days_per_week))
        Income[k]['Period'] = 'weekly'
        
    if Income[k]['Period'] == 'hourly':
        print('How many hours a week do you work at ' + str(k) + '?')
        hours_per_week = input()
        Income[k]['Amount'] = int(Income[k]['Amount'] * int(hours_per_week))
        Income[k]['Period'] = 'weekly'

for k in Income:
    if (int(Income[k]['Amount']) > 550) and (Income[k]['Exempt'] == False):
        print('Up to ' + str(int(Income[k]['Amount'] - 550)) + ' from ' + str(k) +
        ' can be taken from you per week.')
    else:
        print('No money from ' + str(k) + ' can be taken from you. This money is exempt.')

print(Income)

