checking_account = 3200.00
savings_account  = 8500.00
car_value        = 12000.00
home_value       = 220000.00

student_loan     = 18000.00
car_loan         = 6500.00
credit_card_debt = 1200.00
mortgage         = 185000.00

total_assets = checking_account + savings_account + car_value + home_value
total_debts  = student_loan + car_loan + credit_card_debt + mortgage
net_worth    = total_assets - total_debts

print("Your total assets are " + str(total_assets))
print("Your total debts are " + str(total_debts))
print("Your net worth is " + str(net_worth))