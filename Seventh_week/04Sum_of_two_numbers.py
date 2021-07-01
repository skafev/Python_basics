number_1 = int(input())
number_2 = int(input())
magic_number = int(input())
valid_combination = 0
flag = False
for a in range(number_1, number_2+1):
    for b in range(number_1, number_2+1):
        valid_combination += 1
        if a + b == magic_number:
            flag = True
            print(f"Combination N:{valid_combination} ({a} + {b} = {magic_number})")
            break
    if flag:
        break
if not flag:
    print(f"{valid_combination} combinations - neither equals {magic_number}")