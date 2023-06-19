grade = int(input("enter the student grade or -1 to exit"))
total = 0
grade_counter = 0
average = 0

while(grade != -1):
    grade = int(input("enter the student grade or -1 to exit"))
    total +=grade
    grade_counter = +1

if grade_counter != 0:
    average = total / grade_counter
    print(f"the average of student grade is {average}")
else:
    print("no grade were enterd")




