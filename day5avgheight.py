# finding avg height using for loop

student_heights = input("list of students heights").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
sum_heights =0
for heights in student_heights:
    sum_heights += heights

print(sum_heights)

number = 0
for n in student_heights:
    number += 1

print(number)

avg_height = round(sum_heights/number)
print(avg_height)