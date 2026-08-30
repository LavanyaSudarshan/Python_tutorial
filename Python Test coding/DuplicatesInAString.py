str=input("Enter the string ?")
duplicateCount={}

for ch in str:
    duplicateCount[ch]= duplicateCount.get(ch,0)+1

for ch, count in duplicateCount.items():
    if count > 1:
        print(ch, " is repeated ", count, " times")

#using sets
seen = set()
duplicates = set() 

for ch in str:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)

print("Duplicate characters in the string are: ", duplicates)