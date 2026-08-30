str=input("Enter the string ?")
result="".join(dict.fromkeys(str))
print("String after removing duplicates:", result)

result="".join(set(str))
print("String after removing duplicates using set:", result)

result=""
for ch in str:
    if ch not in result:
        result+=ch
print("String after removing duplicates using loop:", result)
