# ref: http://www.nerdparadise.com/tech/interview/fibonacci/
def get_fibonacci_num(n):
    # O(n) - avoiding recursion
    #       'shifting' values left to get new sum
    if n < 3:
        return 1
    sum, fib1, fib2 = 0, 1, 1
    while n > 2:
        # calculate next fib num
        sum = fib1 + fib2
        # 'shift' the numbers left
        # so sum will be a new value
        fib1 = fib2
        fib2 = sum
        n -= 1
    return sum
