# string manipulation 
first_name= "satish" 
last_name= "budanur"
full_name= (first_name + " "+ last_name)# concateation 
print(full_name)
message= "waring!  "
print(message *3)
print(message.upper())
print(message.lower())
print(message.strip()*5)

# soo many methods are like this 
print(len(full_name))# finding length
print(message[4])# indexing = postion-1 
print(message[2:5]) # slicing 
print(message[:4])
print(message[3:])
print(message[::2])# 2 is skiping 
x = "hello! \\  my self satish " # escape squehance \n=new line, \t=tab space ,\\n
print(x)
### examples 
"""Simple Greeting Program: Write a Python program that asks the user
 for their name and age, then prints a personalized greeting message. 
 Use both the + operator and f-strings for output.
"""
name=input("enter your name: ")
age=input("enter your age: ")
print(f" Hello,  {name} you are {age} years old.")
"""
String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace
"""
Name= input("tell me one sentence: ")
print(Name.upper())
print(Name.lower())
print(Name.replace(" ","_"))
print(Name.strip()*9)
"""Character Counter: Write a Python program that:

Asks the user for a string.
Prints how many characters are in the string, excluding spaces."""

s=input("enter the string to calculate the length")
count=len(s.replace(" ",""))
print("num of char:",count)