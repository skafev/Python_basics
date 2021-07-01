number_1 = int(input())
number_2 = int(input())

for number in range(number_1, number_2+1):
    number_to_str = str(number)
    even = 0
    odd = 0

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)

    if even == odd:
        print(number, end=" ")
