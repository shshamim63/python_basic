def take_number():
    while True:
        x=int (input("Enter number1 :"))
        if 1 <= x <= 10**10:
            return x
    
a=take_number()
b=take_number()
print(a+b)
print(a-b)
print(a*b)