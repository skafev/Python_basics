n = int(input())
current = 1
is_bigger = False
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if current > n:
            is_bigger = True
            break
        print(str(current), end=" ")
        current += 1
    if is_bigger:
        break
    print()