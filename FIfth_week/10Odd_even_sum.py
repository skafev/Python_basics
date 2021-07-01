n = int(input())
even = 0
odd = 0
for num in range(1, n + 1):
    number = int(input())
    if num % 2 == 0:
        even += number
    else:
        odd += number
if even == odd:
    print("Yes")
    print(f"Sum = {even}")
else:
    print("No")
    print(f"Diff = {abs(even - odd)}")

