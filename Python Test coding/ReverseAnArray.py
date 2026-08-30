arr= [1,2,3,4,5]
print(arr[::-1])
#print(arr.reverse())
left, right =0, len(arr) -1

while (left < right):
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
