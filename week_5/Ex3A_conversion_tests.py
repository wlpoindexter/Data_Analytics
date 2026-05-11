# Description: This script tests various numeric
# conversion techniques
# Author: Will Poindexter

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# a_int = int(a)   # ValueError: has spaces and decimal point
b_int = int(b)
# c_int = int(c)   # ValueError: contains letters
# d_int = int(d)   # ValueError: contains letters

a_float = float(a)   # Works — Python strips whitespace automatically
b_float = float(b)
# c_float = float(c)  # ValueError: contains letters
# d_float = float(d)  # ValueError: contains letters

a_float_then_int = int(float(a))   # float("101.1") = 101.1 → int = 101

c_num = int(c[:3])   # "402" → 402
d_num = int(d[7])    # "5"   → 5

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(a_float, type(a_float))
print(b_int, type(b_int))
print(b_float, type(b_float))
print(a_float_then_int, type(a_float_then_int))
print(c_num, type(c_num))
print(d_num, type(d_num))

print(a.strip())
print(d.strip())