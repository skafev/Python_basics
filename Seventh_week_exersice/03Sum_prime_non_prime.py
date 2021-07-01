number = input()
not_prime = 0
prime = 0

while number != "stop":
    number = int(number)
    if number < 0:
        print("Number is negative.")
    elif number > 3:

        if number % 2 == 0 or number % 3 == 0:
            not_prime += number
        else:
            prime += number
    else:
        prime += number

    number = input()
print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {not_prime}")