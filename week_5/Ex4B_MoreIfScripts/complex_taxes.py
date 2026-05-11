pay_rate     = 25.00
hours_worked = 45
filing_status = 'single'   

if hours_worked > 40:
    regular_pay  = pay_rate * 40
    overtime_pay = (hours_worked - 40) * pay_rate * 1.5
    weekly_gross = regular_pay + overtime_pay
else:
    weekly_gross = pay_rate * hours_worked

annual_gross = weekly_gross * 52

if filing_status == 'single':
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == 'joint':
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20
else:
    tax_rate = 0.0
    print("Unknown filing status — no tax applied.")

weekly_tax = weekly_gross * tax_rate
net_pay    = weekly_gross - weekly_tax

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${format(pay_rate, '.2f')} per hour, your gross weekly pay is ${format(weekly_gross, '.2f')}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${format(weekly_tax, '.2f')}")
print(f"Your net pay is ${format(net_pay, '.2f')}")