import sys
n = int(input())
even_sum = 0
odd_sum = 0
even_max = -sys.maxsize
even_min = sys.maxsize
odd_max = -sys.maxsize
odd_min = sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if even_max < number:
            even_max = number
        if even_min > number:
            even_min = number

    else:
        odd_sum += number
        if odd_max < number:
            odd_max = number
        if odd_min > number:
            odd_min = number
if n == 0:
    print ( f"OddSum={odd_sum:.2f}," )
    print ( f"OddMin=No," )
    print ( f"OddMax=No," )
    print ( f"EvenSum={even_sum:.2f}," )
    print ( f"EvenMin=No," )
    print ( f"EvenMax=No" )
elif n == 1:
    print ( f"OddSum={odd_sum:.2f}," )
    print ( f"OddMin={odd_min:.2f}," )
    print ( f"OddMax={odd_max:.2f}," )
    print ( f"EvenSum={even_sum:.2f}," )
    print ( f"EvenMin=No," )
    print ( f"EvenMax=No" )
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")