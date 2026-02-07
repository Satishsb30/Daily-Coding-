#tuples
genders = ("male","female","others")
d = ("hello")# when single char use ,
m = (1,2,3,)
l=(4,5,6)
f = m + l # adding more tuples 
print(d)
print(genders)
print(type(genders))
print(genders[2])
print(genders.count("male"))
print("male" in genders)
print(f)
print(genders.index("female"))

# sets
sets = {1,2,3} 
print(sets)
sets1 = {120,45,3522} # o/p is changeable because it's unordered 
print(sets1)
g = {1,2,3}
h={3,4,5}
print(g | h) # union 
print(g & h) # intersection 
print(g-h) # g value is print with delete the value present in the h
print( g ^ h) #symmetric diff
sets.add(9)# adding new element to the set
print(sets)
"""Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.
"""
t= ("alexa","mango","apple","world","hp")
print(t)
# t[0]= "google"
print(t[1:3])
t1=("victus",)
tc= (1,2,3,)
tc1=(4,5,6)
tcs= tc + tc1
print(tcs)
print(type(tcs))

"""Set Operations:

Create two sets: one with your favorite fruits and another with your friend’s 
favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens 
when the fruit doesn’t exist?"" 
"""
# Create two sets
my_fruits = {"apple", "mango", "banana", "orange"}
friend_fruits = {"banana", "grapes", "apple", "kiwi"}

print("My fruits:", my_fruits)
print("Friend's fruits:", friend_fruits)

# Union
print("Union:", my_fruits | friend_fruits)

# Intersection
print("Intersection:", my_fruits & friend_fruits)

# Difference
print("Difference (My - Friend):", my_fruits - friend_fruits)

# Add a new fruit
my_fruits.add("pineapple")
print("After adding pineapple:", my_fruits)

# Remove a fruit using remove()
my_fruits.remove("banana")
print("After removing banana (remove):", my_fruits)

# Remove a fruit using discard()
my_fruits.discard("orange")
print("After discarding orange:", my_fruits)

# What happens if the element does not exist?
# my_fruits.remove("papaya")   # ❌ Raises KeyError
my_fruits.discard("papaya")    # ✅ No error

print("Final set:", my_fruits)

""" Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?"""
# Create a list
elements = ["apple", "banana", "mango", "apple", "orange"]

print("Original list:", elements)

# Convert list to tuple
t = tuple(elements)

# Convert list to set
s = set(elements)

print("Tuple:", t)
print("Set:", s)

# Try to add an element to tuple
# t.append("grapes")   # ❌ AttributeError
# t[0] = "grapes"      # ❌ TypeError

# Try to add an element to set
s.add("grapes")
print("Set after adding grapes:", s)
