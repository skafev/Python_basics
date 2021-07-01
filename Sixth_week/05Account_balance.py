installment = int(input())

installment_made = 0
total = 0

while installment > installment_made:
    money = float(input())
    if money < 0:
        print("Invalid operation!")
        break

    installment_made += 1
    total += money
    print(f"Increase: {money:.2f}")
print(f"Total: {total:.2f}")