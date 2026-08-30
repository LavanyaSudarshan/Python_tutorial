str=input("Enter the string to be reversed?")
arr= list(str)

left, right= 0, len(arr)-1
while left < right:
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp
    left+=1
    right-=1

print("Reversed string is: ", ''.join(arr))