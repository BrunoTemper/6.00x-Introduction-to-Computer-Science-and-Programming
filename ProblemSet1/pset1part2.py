balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

originalBalance = balance

monthlyLowerBound = balance/12
monthlyUpperBound = (balance * (1 + (annualInterestRate)))/12
minimumMonthlyPayment = (monthlyLowerBound + monthlyUpperBound)/2

while balance != 0:
    balance = originalBalance
    for month in range (1,13):
            balance = round(balance - (minimumMonthlyPayment), 2) #paying the monthly
            balance = round(balance + (balance * (annualInterestRate / 12)), 2)
    if balance < 0:
        monthlyUpperBound = minimumMonthlyPayment
    elif balance > 0:
        monthlyLowerBound = minimumMonthlyPayment
    elif balance == 0:
        break
        


print("Lowest payment: " + str(monthlyPayment))
