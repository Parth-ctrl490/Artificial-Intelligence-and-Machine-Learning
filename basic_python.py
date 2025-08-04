#Core Python script for Project 1
print("Hello,World! This is Project 1.")
# Output: Hello,World! This is Project 1.

age=23
print(f"Age: {age},Type:{type(age)}")
# Output: Age: 23,Type:<class 'int'>

h=6.5
print(f"Height:{h},Type:{type(h)}")
# Output: Height:6.5,Type:<class 'float'>

#type conversion
str_num="100"
int_num=int(str_num)
print(f"Converted String:{int_num},Type:{type(int_num)}")
# Output: Converted String:100,Type:<class 'int'>

#Data Structures
fruits=["apple", "banana", "cherry"]
print(f"original list: {fruits}")
# Output: original list: ['apple', 'banana', 'cherry']

fruits.append("Mango")
print(f"updated fruits:{fruits}")
# Output: updated fruits:['apple', 'banana', 'cherry', 'Mango']

fruits.remove("banana")
print(f"updated list:{fruits}")
# Output: updated list:['apple', 'cherry', 'Mango']

fruits.insert(1, "orange")
print(f"final list after insert:{fruits}")
# Output: final list after insert:['apple', 'orange', 'cherry', 'Mango']

removed_fruit=fruits.pop(2)
print(f"Removed fruit: {removed_fruit}, Updated list: {fruits}")
# Output: Removed fruit: cherry, Updated list: ['apple', 'orange', 'Mango']

print(f"First fruit:{fruits[0]}")
# Output: First fruit:apple

print(f"Last fruit:{fruits[-1]}")
# Output: Last fruit:Mango

print(f"fruits count:{fruits[1]}")
# Output: fruits count:orange

#List comprehension
x=[5,6,7,8,9]
sq=[i**3 for i in x]
print(f"cube of number in list:{sq}")
# Output: cube of number in list:[125, 216, 343, 512, 729]

#tuple
tup=("apple", "banana", "cherry")
print(f"tuple:{tup}",type(tup))
# Output: tuple:('apple', 'banana', 'cherry') <class 'tuple'>

#Dictionary
dict={"name":"Parth","age":23,"city":"Dholakpur"}
print(f"Dictionary: {dict}, Type: {type(dict)}")
# Output: Dictionary: {'name': 'Parth', 'age': 23, 'city': 'Dholakpur'}, Type: <class 'dict'>

#dictionary operations
dict1={}
dict1["email"]="parth@gmail.com"
print(f"updated dictionary:{dict1}")
# Output: updated dictionary:{'email': 'parth@gmail.com'}

#sets
unino={1,2,3,3,4,5}
print(f"Set: {unino}, Type: {type(unino)}")
# Output: Set: {1, 2, 3, 4, 5}, Type: <class 'set'>

#Set operations
set1={1,2,3}
set2={3,4,5}
print(f"Union of sets: {set1.union(set2)}")
# Output: Union of sets: {1, 2, 3, 4, 5}

print(f"Intersection of sets: {set1.intersection(set2)}")
# Output: Intersection of sets: {3}

print(f"Difference of sets: {set1.difference(set2)}")
# Output: Difference of sets: {1, 2}

#Control Flow
score=85
if score >=90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
# Output: Grade: B

#enumerate
clr=["red", "green", "blue"]
for index,color in enumerate(clr):
    print(f"Color {index}: {color}")
# Output:
# Color 0: red
# Color 1: green
# Color 2: blue

#while loop
count=0
while count<=5:
    print(f"Count: {count}")
    count+=1
# Output: Count: 0 ... Count: 5

#Break and continue
for i in range(10):
    if i==3:
        print("Skipping 3")
        continue
    if i==8:
        print("Breaking at 8")
        break
    print(i)
# Output: 0,1,2,Skipping 3,4,5,6,7,Breaking at 8

#functions
def greet(name):
    print(f"Hello, {name}!")
print(greet("Parth"))
# Output:
# Hello, Parth!
# None

#Function with default parameters
def cal_area(length, width=1):
    area = length * width
    return area
print(f"Square area: {cal_area(4)}")
# Output: Square area: 4

print(f"Rectangle area: {cal_area(4, 6)}")
# Output: Rectangle area: 24

#function with multiple return values
def get_values(numbers):
    return min(numbers), max(numbers), sum(numbers)
nums = [10, 20, 30, 40]
min_val, max_val, total = get_values(nums)
print(f"Min: {min_val}, Max: {max_val}, Sum: {total}")
# Output: Min: 10, Max: 40, Sum: 100

#Lambda functions
sq=lambda x: x**2
print(f"Square of 5 using lambda: {sq(5)}")
# Output: Square of 5 using lambda: 25

#Lambda with map
num=[1,2,3,4,5]
sq=list(map(lambda x: x**2, num))
print(f"Square of numbers: {sq}")
# Output: Square of numbers: [1, 4, 9, 16, 25]

#Lambda with filter
even_nums=list(filter(lambda x: x % 2 == 0, num))
print(f"Even numbers: {even_nums}")
# Output: Even numbers: [2, 4]

#File I/O
with open("output.txt", "w") as file:
    file.write("Hello,Parth!\n")
    file.write("This is a test file.\n")
    file.write("Goodbye!\n")
# File written

with open("output.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
# Output:
# Hello,Parth!
# This is a test file.
# Goodbye!

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
# Output:
# Hello,Parth!
# This is a test file.
# Goodbye!

#Working with csv files
import csv
csv_data=[
    ["Name", "Age", "City"],
    ["Parth", 23, "Dholakpur"],
    ["Amit", 25, "Delhi"],
    ["Sita", 22, "Mumbai"]
]
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
# CSV written

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Output:
# ['Name', 'Age', 'City']
# ['Parth', '23', 'Dholakpur']
# ['Amit', '25', 'Delhi']
# ['Sita', '22', 'Mumbai']

#working with JSON files
import json
data={
    "name": "Parth",
    "age": 23,
    "city": "Dholakpur",
    "skills": ["Python", "Machine Learning", "Data Science"]
}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
# JSON written

with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("JSON Data:")
    print(loaded_data)
# Output: {'name': 'Parth', 'age': 23, 'city': 'Dholakpur', 'skills': [...]}

#Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
# Output: An error occurred: division by zero

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
finally:
    print("This will always execute.")
# Output: An error occurred: division by zero
#         This will always execute.

try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("This will always execute.")
# Output: Result: 5.0
#         This will always execute.

#Using try-except-finally
try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
finally:
    print("This will always execute.")
# Output: This will always execute.

#Using try-except-else-finally
try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("This will always execute.")
# Output: Result: 5.0
#         This will always execute.

#oops
class Animal:
    species="dog"
    def __init__(self, name,age):
        self.name = name
        self.age=age
    def speak(self):
        return f"{self.name} barks at strangers"
    def info(self):
        return f"{self.name} is a :{self.age} years old"
        
obj1=Animal("tommy",5)
obj2=Animal("bobby",3)
print(obj1.speak())
print(obj1.info())
print(obj2.speak())
print(obj2.info())
# Output:
# tommy barks at strangers
# tommy is a :5 years old
# bobby barks at strangers
# bobby is a :3 years old

#String manipulation  
text="Hello, I am Parth"
print(f"Original text:{text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}") 
print(f"Title case: {text.title()}")
print(f"Reversed: {text[::-1]}")    
print(f"Length: {len(text)}")
print(f"Strip:{text.strip()}")
print(f"Replace 'Parth' with 'Amit': {text.replace('Parth', 'Amit')}")
# Output:
# Original text:Hello, I am Parth
# Uppercase: HELLO, I AM PARTH
# Lowercase: hello, i am parth
# Title case: Hello, I Am Parth
# Reversed: htraP ma I ,olleH
# Length: 17
# Strip:Hello, I am Parth
# Replace: Hello, I am Amit

#String splitting and joining
wrds=text.strip().split()
print(f"Words in text: {wrds}")
joined_text=",".join(wrds)
print(f"Joined text: {joined_text}")
# Output:
# Words in text: ['Hello,', 'I', 'am', 'Parth']
# Joined text: Hello,,I,am,Parth

# String formatting
name = "Alice"
age = 25
score = 95.5
print(f"Student: {name}, Age: {age}, Score: {score:.1f}")
print("Student: {}, Age: {}, Score: {:.1f}".format(name, age, score))
# Output:
# Student: Alice, Age: 25, Score: 95.5
# Student: Alice, Age: 25, Score: 95.5

email = "test@example.com"
print(f"Contains @: {'@' in email}")
print(f"Starts with test: {email.startswith('test')}")
print(f"Ends with .com: {email.endswith('.com')}")
# Output: True, True, True

# Regular expressions (basic)
import re
pattern = r'\b\w+@\w+\.\w+\b'
text_with_emails = "Contact us at info@company.com or support@help.org"
emails = re.findall(pattern, text_with_emails)
print(f"Found emails: {emails}")
# Output: Found emails: ['info@company.com', 'support@help.org']

