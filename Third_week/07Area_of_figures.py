import math
geometric_figure = input()

if geometric_figure == "square":
    side = float(input())
    area = side * side
    print(f"{area:.3f}")

elif geometric_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")

elif geometric_figure == "circle":
    radius = float(input())
    area = math.pi * (radius * radius)
    print ( f"{area:.3f}")

elif geometric_figure == "triangle":
    side_a = float(input())
    side_b = float(input())
    area = (side_a * side_b) / 2
    print ( f"{area:.3f}")