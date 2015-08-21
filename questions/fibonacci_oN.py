# ref: http://www.nerdparadise.com/tech/interview/fibonacci/
def get_fibonacci_num(n):
    # O(n) - avoiding recursion
    #       'shifting' values left to get new sum
    if n < 3:
        return 1
    fib1 = 1
    fib2 = 1
    sum = 0
    while n > 2:
        # calculate next fib num
        sum = fib1 + fib2
        # 'shift' the numbers left
        # so sum will be a new value
        fib1 = fib2
        fib2 = sum
        n-=1
    return sum
