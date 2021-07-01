movie = input()
standard_billet = 0
kid_billet = 0
student_billet = 0

while movie != "Finish":
    free_space = int(input())
    space = 0

    while free_space > space:
        type_of_billets = input()
        if type_of_billets == "standard":
            standard_billet += 1
            space += 1
        elif type_of_billets == "kid":
            kid_billet += 1
            space += 1
        elif type_of_billets == "student":
            student_billet += 1
            space += 1
        elif type_of_billets == "End":
            break
    print(f"{movie} - {(space / free_space) * 100:.2f}% full.")
    movie = input()
total_ticket = student_billet + standard_billet + kid_billet
students = (student_billet / total_ticket) * 100
standard = (standard_billet / total_ticket) * 100
kids = (kid_billet / total_ticket) * 100
print(f"Total tickets: {total_ticket}")
print(f"{students:.2f}% student tickets.")
print(f"{standard:.2f}% standard tickets.")
print(f"{kids:.2f}% kids tickets.")
