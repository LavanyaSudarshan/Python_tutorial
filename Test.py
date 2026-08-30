import os
import sys
import requests

print("Hello World")
text = "Python-is awesome"
#length = len(text)
print("Length of the string:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("String concatenation:", text + " and programming is fun!")
print("Substring (first 6 characters):", text[:6])
print("Substring (after first 6 characters):", text[7:])
print("Substring (Inbetween 7 to 13):", text[7:13])
print("Substring (last 7 characters):", text[-7:])
print("Does the string contain 'awesome'?", "awesome" in text)
print("Replace 'awesome' with 'great':", text.replace("awesome", "great"))
print("Split the string into words:", text.split("-"))
print("Find the index of 'is':", text.find("is"))
print("Count of 'o' in the string:", text.count("o"))
print("String with whitespace removed:", text.strip())
print("String with whitespace removed (lstrip):", text.lstrip())
print("String with whitespace removed (rstrip):", text.rstrip())

# Define configuration variables for a web server
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# Print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

# Update configuration values
port = 443
is_https_enabled = False

# Print the updated configuration
print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enabled}")

students_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
numbers = [1, 2, 3, 4, 5]
print("Student Names:", students_names[0])
print("Length:", len(students_names))

for name in students_names:
    print(name)

for i in range(len(numbers)):
    print(numbers[i])

#argument=input("Please provide a number?")
#argument= sys.argv[1]
#print(argument)
def get_number():
    while True:
        try:
            user_input = int(input(argument))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

Folders= input("Please provide a list of folder names with spaces in between?").split()    
print(Folders)   
for folder in Folders:  
    try: 
     files=os.listdir(folder)
     print(f"Files in {folder}:")
     for file in files:
        print(file)
    except FileNotFoundError:
        print("Please provide a valid folder name " + folder)
        break
    except PermissionError:
        print("You do not have permission to access " + folder)
        break

#dictionary
student_properties = { 
    "Name": "Alice",
    "Age": 20,
    "Grade": "A",
    "Major": "Computer Science"
}
print("Student Name:", student_properties["Name"])
print("Student Age:", student_properties["Age"])

#list of student properties
Property_info =[
    {"Name": "Alice", "Age": 20, "Grade": "A", "Major": "Computer Science"},
    {"Name": "Bob", "Age": 22, "Grade": "B", "Major": "Mathematics"},
    {"Name": "Charlie", "Age": 21, "Grade": "A", "Major": "Physics"}
]
print("First Student Name:", Property_info[0]["Name"])
print("Second Student Age:", Property_info[1]["Age"])


response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_detail = response.json()
for pull_request in complete_detail:
    #print("Pull Request Title:", pull_request["title"])
    print("Pull Request User:", pull_request["user"]["login"])

