arr = [1, 2, 3, 2, 4, 5, 3]

duplicates = {}

for num in arr:
    duplicates[num] = duplicates.get(num, 0) + 1

for key,count in duplicates.items():
    if count > 1:
        print(key)    