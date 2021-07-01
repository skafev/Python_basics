money_needed_for_vacantion = float(input())
money_in_pocket = float(input())
money_spend = 0
days_count = 0
while money_in_pocket > -1:
    command = input()
    money = float(input())
    days_count += 1

    if command == "spend":
        money_in_pocket -= money
        if money_in_pocket < 0:
            money_in_pocket = 0
        money_spend += 1
        if money_spend == 5:
            print(f"You can't save the money.")
            print(days_count)
            break
    elif command == "save":
        money_in_pocket += money
        money_spend = 0
        if money_in_pocket >= money_needed_for_vacantion:
            print(f"You saved the money for {days_count} days.")
            break