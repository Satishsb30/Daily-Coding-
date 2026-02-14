# Lish Comprehension
# # new_list= [expresion for item in collection if condition ]
l= [1,5,8,89,]
dl=[item*2 for item in l]  # item place we any variables # insted of use for loop also for this
print(dl)
l=[x for x in range(1,11)]
print(l)
edl= [even for even in l if even%2==0]
print(edl)
strr= ["fwlh","rtytrewq","sxdwv"]
s=[index[2] for index in strr] 
print(s)

# dic comprehension
names = ["satish","mom","dad","brother"]
dname= {name:len(name) for name in names }  # we list
print(dname)
#
city={
    "bengaluru" :55 ,
    "RNR":44,
    "SSSH":54,
    "kann":10
}
larcity= { key:value for key,value in city.items() if value <=10}
print(larcity)
# taking list of input from user  #string split
s= " l love bengaluru and kannada"
t=s.split()
print(t)
s= " l-love-bengaluru-and-kannada"
o= s.split("-")
print(t)

print("list of input practice")
x= input("Enter list of integers: ")
print(x)
print(x.split())   # out put is string 