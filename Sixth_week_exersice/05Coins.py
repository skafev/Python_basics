change = float(input()) * 100
change = int(change)
coins_counter = 0
while change > 0:
    if change >= 200:
        coins_counter += change // 200
        change %= 200
    if change >= 100:
        coins_counter += change // 100
        change %= 100
    if change >= 50:
        coins_counter += change // 50
        change %= 50
    if change >= 20:
        coins_counter += change // 20
        change %= 20
    if change >= 10:
        coins_counter += change // 10
        change %= 10
    if change >= 5:
        coins_counter += change // 5
        change %= 5
    if change >= 2:
        coins_counter += change // 2
        change %= 2
    if change >= 1:
        coins_counter += change // 1
        change %= 1
print(coins_counter)