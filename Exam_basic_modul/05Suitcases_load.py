capacity = float(input())
free_space = 0
number_of_suitcases = 0

while capacity >= free_space:
    suitcase_volume = input()
    if suitcase_volume == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    suitcase = float(suitcase_volume)
    free_space += suitcase
    number_of_suitcases += 1

    if number_of_suitcases % 3 == 0:
        free_space += suitcase * 0.1

    if free_space > capacity:
        number_of_suitcases -= 1
        print("No more space!")
        break

print(f"Statistic: {number_of_suitcases} suitcases loaded.")