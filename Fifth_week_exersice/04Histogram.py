n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, n + 1):
    number = int(input())
    if number < 200:
        p1 += 1 / n * 100
    elif number <= 399:
        p2 += 1 / n * 100
    elif number <= 599:
        p3 += 1 / n * 100
    elif number <= 799:
        p4 += 1 / n * 100
    else:
        p5 += 1 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")


