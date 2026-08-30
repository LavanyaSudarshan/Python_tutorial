arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8]

result = list(set(arr1) & set(arr2)) #intersection of two sets
print("Common elements in two arrays are: ", result)

result = list(set(arr1) ^ set(arr2))  #symmetric difference
print("Symmetric difference of two arrays is: ", result)
#OR
result = list((set(arr1) - set(arr2)) | (set(arr2) - set(arr1)))
print("Elements that are in either of the arrays but not in both are: ", result)