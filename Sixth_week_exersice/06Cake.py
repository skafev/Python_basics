cake_width = int(input())
cake_length = int(input())

whole_cake = cake_length * cake_width
pieces_count = 0

while whole_cake > 0:
    command = input()
    if command == "STOP":
        print(f"{whole_cake - pieces_count} pieces are left.")
        break
    pieces = int(command)
    pieces_count += pieces
    if pieces_count > whole_cake:
        print(f"No more cake left! You need {pieces_count - whole_cake} pieces more.")
        break
