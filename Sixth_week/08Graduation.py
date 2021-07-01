student_name = input()
to_graduation = 12
average_grade = 0
while to_graduation != 0:
    grade = float(input())
    if grade >= 4:
        average_grade += grade
        to_graduation -= 1
if average_grade >= 4:
    print(f"{student_name} graduated. Average grade: {average_grade / 12:.2f}")
