a=int(input("Enter first number? "))
b=int(input("Enter second number? "))

print("Before swapping: ", a, b)

#a,b=b,a Easy way to swap without using temp variable
a=a+b
b=a-b
a=a-b

print("After swapping: ", a, b)
