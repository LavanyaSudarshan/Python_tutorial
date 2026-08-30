number=int(input("Enter a number to check if it is perfect or not? "))

def isBinary(number):
    while number > 0:
        digit = number % 10
        if digit != 0 and digit != 1:
            return False
        number = number // 10
    return True

print(" The number is binary: ",(isBinary(number)))