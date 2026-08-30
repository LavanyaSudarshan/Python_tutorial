import math
number=int(input("Enter a number to find if its Armstrong or not: "))
sum=0
powerdigits=len(str(number))
temp=number

while ( number > 0):
    digit = number % 10
    sum = sum + math.pow(digit, powerdigits)
    number = number // 10
if  temp == sum:
    print("Armstrong number") 
else:
    print("Not an Armstrong number")      
