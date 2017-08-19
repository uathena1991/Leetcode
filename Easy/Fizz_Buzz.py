def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    for i in range(1,n+1):
        t1 = i%3
        t2 = i%5
        if t1 != 0 and t2 != 0:
            res.append(str(i))
        elif t1 == 0 and t2 != 0:
            res.append('Fizz')
        elif t2 == 0 and t1 != 0:
            res.append('Buzz')
        else:
            res.append('FizzBuzz')
    return res

print fizzBuzz(15)