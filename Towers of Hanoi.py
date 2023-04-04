def _printMove(start, end):
    print(f'{start} --> {end}')

def hanoi(n, start, end):
    if n == 1:
        _printMove(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n-1, start, other)
        _printMove(start, end)
        hanoi(n-1, other, end)

print(hanoi(9, 1, 3))

