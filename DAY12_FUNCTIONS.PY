# functions
def greet():
    print("hello , good morning! ")
greet()

# functions parameters
def marriage(boy,girl): #  parameters ()
    print(f"{boy} married {girl} ")
marriage("satihhh","lfg") # positional arguments
marriage(boy="sinaaa",girl="derf") # keyword arguments

# 
def func(num):
    return int(str(num)*6)
a= 111
b= a + func(2)
print(b)
## parameters
def funn():
    x="chann" # local variable  located in the func
    print("jnfud")
y= "fikiepdo" # global varibale
print(y)
## Greet Function: Write a function greet() that takes no arguments and prints a greeting message.

def greet():
    print("hello, Good mor")
greet()
 # Parameterized Greet: Write a function greet_user() that takes a name as input and prints a custom greeting.
def greet_user(name):
    print(f"Hello, {name} welcome to python course")
greet_user(name="Satish")
def add_numbers(a, b):
    return a + b

# Calling the function with different values
result1 = add_numbers(5, 3)
result2 = add_numbers(10, 20)
result3 = add_numbers(-4, 6)

print("Sum 1:", result1)
print("Sum 2:", result2)
print("Sum 3:", result3)