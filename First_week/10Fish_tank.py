length = int(input())
wide = int(input())
height = int(input())
percent_used_space = float(input()) * 0.01

fish_tank_volume = length * wide * height * 0.001
letter_need = fish_tank_volume * (1 - percent_used_space)

print(f"{letter_need:.3f}")