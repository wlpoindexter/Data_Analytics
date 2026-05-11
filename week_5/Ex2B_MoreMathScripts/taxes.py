salary = 4500.00
tax_rate = 0.23

tax_withheld = salary * tax_rate
net_pay = salary - tax_withheld

print(f"Monthly salary: ${format(salary, '.2f')}")
print(f"Federal tax (23%): ${format(tax_withheld, '.2f')}")
print(f"Take-home pay: ${format(net_pay, '.2f')}")