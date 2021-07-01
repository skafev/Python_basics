destination = input()
budget = float(input())
total = 0

while destination != "End":
    money = float(input())
    total += money
    if total >= budget:
        print(f"Going to {destination}!")
        destination = input()
        if destination == "End":
            break
        budget = float(input())
        total = 0