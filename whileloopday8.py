# while loops
# iteration = attempts
i = 0
while i<=10:
    x = 0
    while x<i:
        print("alexa  "*x)  # if we use while in while= nested while same like nested if 
        x +=1 # first while get executed then while  then x if last x fails then only it go to first while again 
    i +=1
# atm pin
pin ="6969"
trails = 1
while trails<3:
    input_pin = input(f"Trail-{trails} | pin =").strip()
    trails += 1
    if input_pin == pin:
        print("Correct pin")
        break
    else:
        print("Wrong pin")

 # EXamples
"""Basic Counting with while Loop:

Write a program that counts from 1 to 10 using a while loop."""
count= 1
while count<=10:
    print(count)
    count +=1

"""Odd Numbers Printer:

Create a program that prints all odd numbers between 1 and 20 using a while loop."""
Count = 1
c = 1
while c<=20:
    c=int(input("Enter the value to check odd: "))
    if not(c %2 ==0):
        print("its odd")
        break
    else:
        print("even")
"""Odd Numbers Printer:

Create a program that prints all odd numbers between 1 and 20 using a while loop."""    
Co = 1

while Co <= 20:
    if Co % 2 != 0:
        print(Co)
    Co += 1
"""
Ticket Booking Simulation:

Write a program that simulates a bus ticket booking system.
The bus has 8 seats. Each time a seat is booked, the available seats decrease. 
When there are no seats left, the loop stops and displays a message saying "All seats are booked."""
seats = 8

while seats > 0:
    print("Seat booked successfully!")
    seats -= 1
    print("Available seats:", seats)

print("All seats are booked.")

"""Countdown Timer:

Write a program that counts down from 10 to 1 using a while loop and 
prints "Happy New Year!" after the countdown is over."""
down = 10
while down >=1:
    print("Count down start!!!!")
    down -=10
    print("remaing time: ",down)
print("Happy new year")

num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")

numbers = [10, 20, 30, 40]
key = 25

for n in numbers:
    if n == key:
        print("Found")
        break
else:
    print("Not Found")
