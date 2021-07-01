n = int(input())
total = 0
total_two = 0
for _ in range(n):
    number = int(input())
    total += number

for _ in range(n):
    number = int(input())
    total_two+= number

if total == total_two:
    print(f"Yes, sum = {total}")
else:
    print(f"No, diff = {abs(total - total_two)}")