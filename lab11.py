# counter
average_counter = 0
grade = []

#inputs
student_num =int(input("Enter how many students: "))

#calculation
for i in range(student_num):
        student_grade = float(int(input(f"Enter Student Grade {student_num}: ")))
    if student_grade < 40 or student_grade > 100:
        print("Error. Invalid Grade")
    break
grade.append(student_grade)
if student_grade >= 45:
        average_counter += 1

if student_grade < 40 or student_grade > 100:
    exit()

# calculation
overall_grade = (sum(grade)/(student_num))
passing_grade = (average_counter/student_num)*100

print(f"Average grades of {student_num} students:" , overall_grade)
print("Numbers of students with passing grade: " , str(average_counter))
print("Passing percentage (%): " , passing_grade , "%")
