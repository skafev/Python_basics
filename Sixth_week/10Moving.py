width = int(input())
length = int(input())
height = int(input())

space_house = width * length * height
enough_space = True
boxes_in = 0
while enough_space:
    command = input()
    if command == "Done":
        print(f"{space_house - boxes_in} Cubic meters left.")
        break
    box = int(command)
    boxes_in += box
    if boxes_in > space_house:
        print(f"No more free space! You need {boxes_in - space_house} Cubic meters more.")
        break