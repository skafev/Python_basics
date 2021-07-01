student_name = input()
to_graduation = 1
average_grade = 0
to_be_expelled = 0
while to_graduation <= 12:
    grade = float(input())
    if grade >= 4:
        average_grade += grade
        to_graduation += 1
    else:
        to_be_expelled += 1
        if to_be_expelled == 2:
            print(f"{student_name} has been excluded at {to_graduation} grade")
            break
if average_grade >= 4 and to_graduation == 13:
    print(f"{student_name} graduated. Average grade: {average_grade / 12:.2f}")