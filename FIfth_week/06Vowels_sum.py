text = input()
total = 0

for n in text:
    if n == "a":
        total += 1
    elif n == "e":
        total += 2
    elif n == "i":
        total += 3
    elif n == "o":
        total += 4
    elif n == "u":
        total += 5

print(total)