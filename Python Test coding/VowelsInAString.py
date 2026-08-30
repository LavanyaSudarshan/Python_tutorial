str=input("Enter the string")
count=0

for ch in str:
    if ch in 'aeiouAEIOU':
        count+=1
print("Number of vowels in the string is: ", count)

VowelCount={}
for ch in str.lower():
    if ch in 'aeiou':
            VowelCount[ch]= VowelCount.get(ch,0)+1

print("Vowel count in the string is: ", VowelCount)        