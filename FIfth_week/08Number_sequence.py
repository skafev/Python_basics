n = int(input())
max_number = -100000
min_number = 100000

for number in range(n):
    num = int(input())
    if number == 0:
        min_number = num
        max_number = num
    else:
        if num > max_number:
            max_number = num
        elif num < min_number:
            min_number = num
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")