steps_goal = 10000
steps_count = 0
while steps_goal > 0:
    steps_making = input()
    command = str(steps_making)
    if command == "Going home":
        steps_making = int(input())
        steps_count += steps_making
        if steps_count >= steps_goal:
            print("Goal reached! Good job!")
        else:
            print(f"{steps_goal - steps_count} more steps to reach goal.")
        break
    steps_count += int(steps_making)
    if steps_count >= steps_goal:
        print("Goal reached! Good job!")
        break