world_record = float(input())
distance = float(input())
time = float(input())
add_time = distance // 15 * 12.5
sum_time = distance * time + add_time

if sum_time < world_record:
    print(f"Yes, he succeeded! The new world record is {sum_time:.2f} seconds.")
else:
    new_record = sum_time - world_record
    print(f"No, he failed! He was {new_record:.2f} seconds slower.")