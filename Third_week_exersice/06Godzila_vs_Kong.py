budget = float(input())
statist_count = int(input())
statist_gear = float(input())

decor = budget * 0.1
statist_gear = statist_count * statist_gear
if statist_count > 150:
    statist_gear = statist_gear - statist_gear * 0.1

final_budget = decor + statist_gear
total = abs(budget - final_budget)
if final_budget > budget:
    print("Not enough money!")
    print(f"Wingard needs {total:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {total:.2f} leva left.")