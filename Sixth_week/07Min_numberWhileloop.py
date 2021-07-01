n = int(input())

smallest_number = 10000
number_counter = 0

while n > number_counter:
    number = int(input())
    if number < smallest_number:
        smallest_number = number
    number_counter += 1
print(smallest_number)