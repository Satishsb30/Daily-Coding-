# for loops
i =1
while i<=10:
    print(i ,end="  ") # print(i) = print the numbers in one by one 
    i+=1
print("")

for i in range(1,11,2): # syntax for items in items    and while slicing e use ;:2 here we use ,,2 skiping one number ,,3 ski 2 number 
    print(i,end="  ")
print()    
    

bag = ["Red","orange","green"]
for ball in bag:  # that ball in that what ever we can write 
    print(ball)
print()

x = "Satish "
for letter in x :
    print((x) * 5)

for index,letter in enumerate(x):   # index and letter its a unpacking 
    print(letter*(index+1))

l = ["11", "65459","55897","5285"]
for index,num in enumerate(l):   # index and letter its a unpacking 
    print(f"{num } is in {index}th index")

# using dic
d= { "name": "Satish","age":20,"class":12} 
for key, value in d.items():   # d.items is  converting list of tuples 
    print(key ," " ,value)
#nested loops
# multiplication tables 
for i in range(1,11):
    print(f"2x{i}={2*i}")  # this for only 2 tables

for i in range(2,11) :
    for j in range (1,11) :
        print(f"{i}X {j} = {i*j}"  ) # this for 2 to 10 tables 

"""Multiples of 3:

Write a for loop that prints all multiples of 3 between 1 and 30."""
for z in range(3,31,3):
    print(z)

"""Sum of First 10 Numbers:
Write a program using a for loop that calculates the sum of numbers from 1 to 10."""
total=0
for i in range(1,11):
    total+=i
print("sum:",total)

"""Print Your Name Letter by Letter:

Write a program that takes your name as input and prints each letter of your name using a for loop."""
name=input("Enter ur name:")
for n in name:
    print(n)

"""Count Vowels in a String:

Write a program that counts how many vowels are in a given string using a for loop"""

count = 0
text=input("Enter ur string: ")
for c in text:
    if c in "aeiouAEIOU":
        count +=1
print("number of vowels in ur string : ",count)