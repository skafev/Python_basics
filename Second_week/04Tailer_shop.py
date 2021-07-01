tables_count = int(input())
length_meters = float(input())
width_meters = float(input())

tablecloth = (length_meters + 2 * 0.3) * (width_meters + 2 * 0.3) * tables_count
square = (length_meters / 2) * (length_meters / 2) * tables_count

cost_in_usd = tablecloth * 7 + square * 9
cost_in_bgn = cost_in_usd * 1.85

print(f"{cost_in_usd:.2f} USD")
print(f"{cost_in_bgn:.2f} BGN")