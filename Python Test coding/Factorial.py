number=int(input("Enter a number to find it is factorial "))
fact=1

for i in range(1, number+1):
    fact=fact*i
print("Factorial of ", number, "is ", fact)

def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number-1)
print(factorial(number))