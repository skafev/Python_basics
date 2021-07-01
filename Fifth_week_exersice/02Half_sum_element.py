n = int(input())
biggest = -1000
all_numbers = 0
for i in range(n):
    number = int(input())
    all_numbers += number
    if number > biggest:
        biggest = number
if (all_numbers - biggest) == biggest:
    print("Yes")
    print(f"Sum = {biggest}")
else:
    print("No")
    print(f"Diff = {abs(biggest - (all_numbers - biggest))}")