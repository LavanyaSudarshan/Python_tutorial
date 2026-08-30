number=int(input("Enter a number to check if it is perfect or not? "))
sum=0
for i in range(1, number // 2 + 1):
    if number % i ==0:
        sum+=i
if sum == number:
    print("Perfect number") 
else:
    print("Not a perfect number")           