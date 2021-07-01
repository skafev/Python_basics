name = input()
password = input()
credentials = input()
while password != credentials:
    credentials = input()
print(f"Welcome {name}!")