#lists 
items = ["mango","apple","fish"]
print(items)
print(items[1]) # accesing using index
print(items[-1]) # -ve indexing 
# modifiying elements
items.append("mutton") # adding only by the end of list
print(items)
items.insert(3,"chicken") # inserting whereever we want
print(items)
items.pop() # removing last one
print(items)
items.pop(0) # removing first one 
print(items)
items.remove("fish") # remove selected 
print(items)
items.clear
print(items)
# slicing
l= ["man","women","boy","fruit","300","500","man","man"]
print(l)
print(l[0:4])
print(l[:5])
print(l[1:])
print(l[::2])
print(l[1::2])
# functions
print(len(l))
print(sorted(l))
print("Boy is present at 'l' index:",l.index("boy"))
print(l.count("man"))
l.reverse()
print(l)
# nested lists
matrix = [[1,2,15],[11,12,14],[12,1,5]]
print(matrix)
print(matrix[0])
print(matrix[0][2])

"""example problems
 List Manipulation Exercise:

Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation."""

items1 = [10, 20, 30, 40, 50]
print("Initial list:", items1)
items1.append(60)
print("After adding item at the end:", items1)
items1.insert(1, 15)
print("After adding item at second position:", items1)
items1.pop(2)
print("After removing the third item:", items1)

"""Reverse and Sort a List: Create a list of numbers and:

Sort it in descending order.
Reverse the sorted list and print it."""

numbers = [5, 2, 9, 1, 7, 3]
print("Original list:", numbers)
numbers.sort(reverse=True)
print("Sorted in descending order:", numbers)
numbers.reverse()
print("Reversed list:", numbers)
