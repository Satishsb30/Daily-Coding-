#COnditional Statementes 
x = 10
if x==10:
    print("x value is 10") # that tab space is known as indentation 
else:
    print("X is not 10")
# another examples
Y= int(input("Enter the value to find Even or odd: "))
if  Y % 2 == 0:
    print("Y is even")
else:
    print("Y is odd")
# signal example with elif
s = input("Enter the colour to fid signal: ")
if s=="red":
    print("Stop")
elif s=="green":
    print("Get ready") # elif we several time with our i/p 
elif s=="black":
    print("nothing")
elif s == "green":
    print("chal")
else:
    print("")

age = int(input("Enter your age: "))

if age >= 18:  # comparision opeerator
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


age = 16    # logical operator And , or, 
has_student_id = True

if age < 18 and has_student_id:
    print("You are eligible for the student discount!")
else:
    print("You are not eligible for the student discount.")

gender =input("Enter ur gender: ")
Age = int(input("Enter ur Age: "))
if gender=="female":
    print("you are eligible for Free ticket")
elif Age<=13:
    print("eligible")
elif Age>=60:
    print("eligible")
else:
    print("Not Eligible")
##  


day = "Saturday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")



"""Write a program to check if someone is eligible for a bus pass.
 If they are below 5 years, the bus pass is free. If they are 60 years or older,
   they get a senior citizen discount. Otherwise, they pay the full price"""
buss  = int(input("Enter your age: "))
if buss<5:
    print("Eligible for buss pass is free")
elif buss>=60:
    print("Eligible for buss pass is free in senior citizen discount")
else:
    print("You pay the full price  ")

"""Meal Time Checker:

Create a program that checks the time of day (24-hour format) and prints whether 
it's time for breakfast, lunch, or dinner.
Breakfast: 8 AM
Lunch: 1 PM
Dinner: 8 PM
If none of these times, print "It's not meal time."""

M= int(input("What is the time now: "))
if M==8:
    print("Time for Breakfast")
elif M==13:
    print("Time for Lunch")
elif M==20:
    print("Time for Dinner")
else:
    print("It's not time for meal")

"""Simple Eligibility Check:

Write a program that checks whether a person is eligible for a library membership. 
If they are under 18, they get a student membership. If they are 60 or older, 
-they get a senior citizen membership. Otherwise, they get a regular membership."""

age =int(input("Enter your age: "))

if age <18:
    print("You got a Student membership")
elif age >= 60:
    print("You got a senior citizen membership")
else:
    print("you got a regular membership")
