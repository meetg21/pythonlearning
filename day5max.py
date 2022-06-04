student_marks = input("list of students heights").split()
for n in range(0,len(student_marks)):
    student_marks[n]=int(student_marks[n])
print(student_marks)
maximum_marks = 0
for maximum in student_marks:
    if maximum > maximum_marks:
        maximum_marks = maximum
    
print(maximum_marks)

    