n = int(input())

biggest_number = -10000
number_counter = 0

while n > number_counter:
    number = int(input())
    if number > biggest_number:
        biggest_number = number
    number_counter += 1
print(biggest_number)