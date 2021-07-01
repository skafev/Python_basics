command = input()
total = 0

while command != "Stop":
    number = int(command)
    total += number
    command = input()
print(total)
