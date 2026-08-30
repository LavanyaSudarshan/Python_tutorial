number=12345
reversedNumber=0

while number!=0:
    digit=number%10
    reversedNumber = reversedNumber *10 + digit
    number=number//10
print(reversedNumber)   
