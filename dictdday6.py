# Dictionaries Operations
IPL_captians = {
    "RCB": "virat ",  # "key" : "value"
    "CSK": "Dhoni",
    "RR": "Vaibhav",
    "LSG": "KL R"
}
print(IPL_captians)
print(type(IPL_captians))
print(IPL_captians["RCB"]) # ACCESING 
print(IPL_captians.get("PJ"),"notfound" ) # oif we put direct print(IPL_captians[PJ]) : it's crash the program so we use get fun
IPL_captians["GJ"] = "hardik"  # adding new in RUN time  also same for updating 
print(IPL_captians)
IPL_captians.pop("RR") # OR : del IPL_captians["RR"]
print(IPL_captians)
# methods
print(IPL_captians.keys())
print(IPL_captians.values())
print(IPL_captians.items())
ICC= {"T20": "india"}
IPL_captians.update(ICC)
print(IPL_captians)
# we use char : str, str: char,str: bool , any type we use except list
"""Basic Dictionary Operations:

Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
Add a new city and its dish to the dictionary.
Update the dish for Bengaluru.
Remove one city from the dictionary.
Use the keys() method to print all city names in the dictionary.
Use the values() method to print all dishes in the dictionary."""
# Step 1: Create a dictionary with 5 cities in Karnataka and their famous dishes
karnataka_dishes = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Hubballi": "Girmit",
    "Mangaluru": "Neer Dosa",
    "Ballari": "Kotte Kadubu"
}

print("Initial Dictionary:")
print(karnataka_dishes)

# Step 2: Add a new city and its famous dish
karnataka_dishes["Shivamogga"] = "Akki Rotti"
print("\nAfter Adding Shivamogga:")
print(karnataka_dishes)

# Step 3: Update the dish for Bengaluru
karnataka_dishes["Bengaluru"] = "Ragi Mudde"
print("\nAfter Updating Bengaluru's Dish:")
print(karnataka_dishes)

# Step 4: Remove one city from the dictionary
karnataka_dishes.pop("Ballari")
print("\nAfter Removing Ballari:")
print(karnataka_dishes)

# Step 5: Print all city names using keys()
print("\nCity Names:")
print(karnataka_dishes.keys())

# Step 6: Print all dishes using values()
print("\nFamous Dishes:")
print(karnataka_dishes.values())
"""
# Nested Dictionary Practice (Simple for now):

Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
Access and print the favorite food of one friend."""
# Step 1: Create a nested dictionary for two friends
friends = {
    "friend1": {
        "name": "Rahul",
        "favorite_subject": "Mathematics",
        "favorite_food": "Dosa"
    },
    "friend2": {
        "name": "Anita",
        "favorite_subject": "Computer Science",
        "favorite_food": "Pulao"
    }
}

# Step 2: Access and print the favorite food of one friend
print("Favorite food of Rahul:")
print(friends["friend1"]["favorite_food"])


