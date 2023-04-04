def multiply(a, b):
    if b == 1:
        return a
    else:
        return a + multiply(a, b-1)

def power(base, exp):
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)

def print_range_up(n):
    def rec(n):
        if n == 0:
            return '0'
        else:
            return str(n) + '\n' + str(rec(n-1))
    print(rec(n))

def print_range_down(n):
    def rec(n):
        if n == 0:
            return '0'
        else:
            return str(rec(n-1)) + '\n' + str(n)
    print(rec(n))

def string_reverse(phrase):
    if len(phrase) == 1:
        return phrase[0]
    else:
        return string_reverse(phrase[1:]) + phrase[0]

def is_prime(n):
    number = n
    n -= 1 
    def rec_prime(number, n):
        if n == 1:
            return 0
        else:
            if number % n == 0:
                return 1 + rec_prime(number, n-1)
            else:
                return 0 + rec_prime(number, n-1)
    total = rec_prime(number, n)
    if total == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def properties_of_n(n):
    strn = str(n)
    powers = (strn + ' to the power of ' + strn + ' is ' + str(power(n, n)) + '\n')
    prime = ('Is ' + strn + ' a prime number? ' + str(is_prime(n)) + '\n')
    fib = ('The ' + strn + 'th value in the fibonacci sequence is ' + str(fibonacci(n)) + '\n')

    return  powers + prime + fib



