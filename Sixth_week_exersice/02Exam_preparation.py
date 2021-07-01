bad_grades = int(input())
problems_solved = 0
average_score = 0
last_problem_solved = ""
total_bad_grades = 0
not_enough = True
while not_enough:
    text = input()
    if text == "Enough":
        print(f"Average score: {average_score / problems_solved:.2f}")
        print(f"Number of problems: {problems_solved}")
        print(f"Last problem: {last_problem_solved}")
        break
    last_problem_solved = text
    score = int(input())
    if score <= 4:
        total_bad_grades += 1
        if total_bad_grades == bad_grades:
            print(f"You need a break, {total_bad_grades} poor grades.")
            break

    problems_solved += 1
    average_score += score