# Ram Loves Sita 
boy_name = input("Boy name: ")
boy_age = int(input("Boy Age: "))
girl_name = input("Girl name: ")
girl_age = int(input ("Girl Age: "))

age_diff = boy_age - girl_age
print(age_diff)
print(
    boy_name, girl_name)#normal

print(boy_name +" Loves "+ girl_name +" Age difference is "+  str(age_diff ))  #concatenated str
print(f"{boy_name} Loves {girl_name} Age diifrence is {age_diff}")# formatated str