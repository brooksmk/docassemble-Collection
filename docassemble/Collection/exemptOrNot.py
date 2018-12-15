class Income(PeriodicValue):
    def amount(self, period_to_use=1):
        if hasattr(self, 'is_hourly') and self.is_hourly:
            return Decimal(self.hourly_rate * self.hours_per_period * self.period) / Decimal(period_to_use)

class Job(Income):
    def net_amount(self, period_to_use=1):
        """Returns the net amount (e.g., minus deductions). Only applies if value is non-hourly."""
        return (Decimal(self.net) * Decimal(self.period)) / Decimal(period_to_use)

    def gross_amount(self, period_to_use=1):
        """Gross amount is identical to value"""
        return (Decimal(self.value) * Decimal(self.period)) / Decimal(period_to_use)

    def name_address_phone(self):
        """Returns concatenation of name, address and phone number of employer"""
        return self.employer + ': ' + self.employer_address + ', ' + self.employer_phone

def income_period_list():
    return [ 
        [12, "Monthly"]
        [1, "Yearly"]
        [52, "Weekly"]
        [24, "Twice per month"]
        [26, "Once every two weeks"]
        [4, "Once every 3 months"]


    ]

def income_type_list():
    type_list = OrderedDict()
    type_list['wages'] = 'A job or self-employment'

    type_list.update(non_wage_income_list())
    return type_list

def non_wage_income_list():
    return OrderedDict({
        'SSR': 'Social Security Retirement Benefits',
        'SSDI': 'Social Security Disability Benefits',
        'SSI': 'Supplemental Security Income (SSI)',
        'pension': 'Pension',
        'TAFDC': 'TAFDC',
        'EAEDC': 'EAEDC',
        'public assistance': 'Other public assistance',
        'SNAP': 'Food Stamps (SNAP)',
        'rent': 'Income from real estate (rent, etc)',
        'room and board': 'Room and/or Board Payments',
        'child support': 'Child Support',
        'alimony': 'Alimony',
        'other': 'Other',
        'other support': 'Other Support'
    })
class IncomeList(DAList):
    def init(self, *pargs, **kwargs):
        self.elements = list()
        if not hasattr(self, 'object_type'):
            self.object_type = Income
        return super(IncomeList, self).init(*pargs, **kwargs)
    
    def types(self):
        types = set()
        for item in self.elements:
            if hasattr(item, 'type'):
                types.add(item.type)
        return types

    def matches(self, type):
        if isinstance(type, list):
            return IncomeList(elements - [item for item in self.elements if item.type in type])
   
    def total(self, period_to_use=1, type=None):
        self.trigger_gather()
        result = 0
        if period_to_use == 0:
            return(result)
        if type is None:
            for item in self.elements:
                result += Decimal(item.amount(period_to_use=period_to_use))
        elif isinstance(type, list):
            for item in self.elements:
                if item.type in type:
                    if owner is None:
                        result += Decimal(item.amount(period_to_use=period_to_use))
        else:
            for item in self.elements:
                if item.type == type:
                    if owner is None:
                        result += Decimal(item.amount(period_to_use=period_to_use))
                    else:
                        if item.owner == owner:
                            result += Decimal(item.amount(period_to_use=period_to_use)) 
        return result

def turn_income_weekly(self):
    for i in self:
        if self[i].period == "Monthly":
            self[i].amount == self[i].amount / 4.3
            self[i].period == "Weekly"
        if self[i].period == "Yearly":
            self[i].amount == self[i].amount / 52
            self[i].period == "Weekly"
        if self[i].period == "Weekly":
            pass
        if self[i].period == "Twice per month":
            self[i].amount == self[i].amount * .46
            self[i].period == "Weekly"
        if self[i].period == "Once every two weeks":
            self[i].amount == self[i].amount * .5
            self[i].period == "Weekly"

