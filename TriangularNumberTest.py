#Tests if the number is a prime number using recursion. If it is, it prints out which triangular number it is
def TriangularNumberTest(x, count = 1):
    z = 1 + count
    if x < 0:
        return False
    elif x == 0:
        print('It is the ' + str(count-1) + 'th triangular number.')
        return True
    else:
        return TriangularNumberTest(x-count, z)

