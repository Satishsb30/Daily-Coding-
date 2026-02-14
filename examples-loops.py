# sum using for loops in lists
l= [45,5,55,2,55]
print(sum(l))  # without loops
total =0
print("after loops")
for num in l :
    total+=num
    print(total)

# doubleing nuber
dl=[]
for i in l:
    dl.append(i*2)
    print(dl)

#  loops in dict
student_marks= { "alexa": "55","bob":"58","meft":88,"sathii":100}
for student in student_marks.keys():  # also use like student in student_marks.keys() 
    print(student)

for marks in student_marks.values(): # also use like student in student_marks.values() 
    print(marks)
for student , marks in  student_marks.items():   # also use like student in student_marks.items() 
    print(f"{student}=={marks}")

