# introduction to the number variable
base_pay = 17000
addition_pay = 12000
income = base_pay + addition_pay
tax_to_pay = base_pay * 0.15

print(tax_to_pay)
print(income - tax_to_pay)

# introduction to the string

income_text = 'total income: '
tax_text = "tax needs to be paid: "

print(income_text + str(income - tax_to_pay))
print(tax_text + str(tax_to_pay))
print(income_text[-2])
print(tax_text[::2])
print(tax_text[::-1])
print('T' + tax_text[1::])

print(income_text.upper())
print(income_text.lower())
print('T' + '-'.join(tax_text.split())[1::])