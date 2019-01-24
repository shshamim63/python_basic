def number_input():
    while True:
        N=int(input("Enter number:"))
        if 1 <=  N <= 20 :
            return N
p=number_input()
for i in range(p):
    print(i**2)
