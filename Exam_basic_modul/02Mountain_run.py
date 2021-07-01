import math
record_in_sec = float(input())
distance = float(input())
time_in_sec = float(input())

time_slowed = math.floor(distance / 50)
plus_time = time_slowed * 30
total_time = (time_in_sec * distance) + plus_time

if total_time < record_in_sec:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time - record_in_sec:.2f} seconds slower.")