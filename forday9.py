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
