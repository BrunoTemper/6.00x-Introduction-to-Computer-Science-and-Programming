balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


totalPaid = 0
for month in range (1,13):
    minimumMonthlyPayment = round(balance * monthlyPaymentRate, 2)
    balance = round(balance - (minimumMonthlyPayment), 2) #paying the monthly
    balance = round(balance + (balance * (annualInterestRate / 12)), 2)
    
    totalPaid = round(minimumMonthlyPayment + totalPaid, 2)


    print('Month:'  +  str(month))
    print('Minimum monthly payment: ' + str(minimumMonthlyPayment))
    print('Remaining balance: ' + str(balance))

print("Total paid: " + str(totalPaid))
print("Remaining balance: " + str(balance))
