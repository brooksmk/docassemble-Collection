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

