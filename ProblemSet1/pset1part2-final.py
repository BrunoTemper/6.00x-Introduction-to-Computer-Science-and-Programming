balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

originalBalance = balance
monthlyPayment = 0

while balance > 0 :
    balance = originalBalance
    monthlyPayment +=10
    minimumMonthlyPayment = monthlyPayment
    for month in range (1,13):
            balance = round(balance - (minimumMonthlyPayment), 2) #paying the monthly
            balance = round(balance + (balance * (annualInterestRate / 12)), 2)

print("Lowest payment: " + str(monthlyPayment))

