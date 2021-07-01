number = float(input())
metric_to_convert = input()
final_metric = input()

if metric_to_convert == "mm" and final_metric == "m":
    number /= 1000
elif metric_to_convert == "m" and final_metric == "cm":
    number *= 100
elif metric_to_convert == "cm" and final_metric == "mm":
    number *= 10
elif metric_to_convert == "m" and final_metric  == "cm":
    pass
print(f"{number:.3f}")