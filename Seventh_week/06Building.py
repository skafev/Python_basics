number_of_floors = int(input())
number_of_rooms = int(input())

for n in range(number_of_floors, 0, -1):
    for j in range(0, number_of_rooms):

        if n == number_of_floors:
            print(f"L{n}{j}", end=' ')
            continue

        if n % 2 == 0:
            print(f"O{n}{j}", end=' ')
        else:
            print(f"A{n}{j}", end=' ')
    print()
