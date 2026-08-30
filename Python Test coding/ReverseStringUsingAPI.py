s="lavanya"
reverse_string = s[::-1] #this is built in slicing
print(reverse_string)

s1="Hello"
reverseString = ''.join(reversed(s1)) # reversed is built in function 
                                      # which takes a string and 
                                      # returns characters in reverse.
                                      # join combines them into String
print(reverseString)

lst = ['h', 'e', 'l', 'l', 'o']
lst.reverse() #reverse works only for lists
print(lst)