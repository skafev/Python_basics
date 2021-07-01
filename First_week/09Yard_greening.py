yard_to_green = float(input())
without_discount = yard_to_green * 7.61
total = without_discount - without_discount * 0.18
discount = without_discount - total

print(f"The final price is: {total:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")
