#operators 
a=3
a+=10# equals to a=a+10
print(a)# assignment operators +=,-=,*=,/=..
b = 20

print(a == b)  # comparision operators 
print(a != b)
print(a > b) 
print(a < b) 
print(a >= 10)  
print(b <= 25) 
x = 5
y = 10
z = 15

#Logical operators  and operator
print(x > 0 and y > 5)  

# or operator
print(x > 10 or z > 10) 
# not operator
print(not(x > 10)) 
# memebership operators 
my_list = [1, 2, 3, 4, 5]
my_string = "Python"

print(3 in my_list) 
print(6 not in my_list) 
print("P" in my_string)
print("z" not in my_string)
a = 5  # In binary: 101
b = 3  # In binary: 011

# Bitwise AND
print(a & b) 
# Bitwise OR
print(a | b)  
# Bitwise XOR
print(a ^ b) 
# Bitwise NOT
print(~a) 
# Left shift
print(a << 1)  
# Right shift
print(a >> 1) 
""" examples works 
Logical Operator Practice: Write a Python program that takes two numbers as input
 from the user and checks if:

Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not)."""
s=int(input("Enter first number: "))
s2=int(input("Enter second number: "))
print("Both numbers are greather than 10 :",s>10 and s2>10 )
print("At least one of the numbers is less than 5:",s<5 or s2<5)
print("The first number is not grather than the second (usingnot):",not(s>s2))
"""Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:

"You are an adult" if the age is greater than or equal to 18.
"You are a minor" if the age is less than 18.
Use >= and < comparison operators.
"""
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
elif age < 18:
    print("You are a minor")


