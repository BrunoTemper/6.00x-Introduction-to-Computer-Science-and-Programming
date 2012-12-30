balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

originalBalance = balance

monthlyLowerBound = balance/12
monthlyUpperBound = (balance * (1 + ((annualInterestRate)**12)/12))
minimumMonthlyPayment = 0

while balance != 0:
    balance = originalBalance
    minimumMonthlyPayment = (monthlyLowerBound + monthlyUpperBound)/2
    for month in range (1,13):
            balance = round(balance - (minimumMonthlyPayment), 2) #paying the monthly
            balance = round(balance + (balance * (annualInterestRate / 12)), 2)
    if (balance + .05) < 0:
        monthlyUpperBound = minimumMonthlyPayment
    elif (balance - .05) > 0:
        monthlyLowerBound = minimumMonthlyPayment
    elif -.5 < balance < .5:
        
        #(balance < .05) || (balance > .05):
        break


print("Lowest payment: " + str(round((minimumMonthlyPayment),2)))
