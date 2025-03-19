# ANSWER QUESTION wwpd

def takeWhile(t, p):
    """Take elements from t until p is not satisfied.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> list(takeWhile(s, lambda x: x == 10))
    [10]
    >>> s2 = iter([1, 1, 2, 3, 5, 8, 13])
    >>> list(takeWhile(s2, lambda x: x % 2 == 1))
    [1, 1]
    >>> s = iter(['a', '', 'b', '', 'c'])
    >>> list(takeWhile(s, lambda x: x != ''))
    ['a']
    >>> list(takeWhile(s, lambda x: x != ''))
    ['b']
    >>> next(s)
    'c'
    """
    "*** YOUR CODE HERE ***"
    try:
        while True:
            x = next(t)
            if p(x):
                yield x
            else:
                break
    except StopIteration:
        pass
    
    '''
    list=[]
    while True:
        x = next(t)
        if p(x):
            list.append(x)
        else:
            break
    return list
    '''


def backAndForth(t):
    """Yields and skips elements from iterator t, back and forth.

    >>> list(backAndForth(iter([1, 2, 3, 4, 5, 6, 7, 8, 9])))
    [1, 4, 5, 6]
    >>> list(backAndForth(iter([1, 2, 2])))
    [1]
    >>> # generators allow us to represent infinite sequences!!!
    >>> def naturals():
    ...     i = 0
    ...     while True:
    ...         yield i
    ...         i += 1
    >>> m = backAndForth(naturals())
    >>> [next(m) for _ in range(9)]
    [0, 3, 4, 5, 10, 11, 12, 13, 14]
    """
    "*** YOUR CODE HERE ***"
    try:
        i=1
        while True:
            if i % 2 == 1:
                for _ in range(i):
                    yield next(t)
                i += 1
            else:
                for _ in range(i):
                    next(t)
                i += 1
    except StopIteration:
        pass

    '''
    i = 1
    list=[]
    try:
        while True and i<=30:

            if i % 2 == 1:
                for _ in range(i):
                    list.append(next(t))
                i += 1
            else:
                for _ in range(i):
                    next(t)
                i += 1
    except StopIteration :
        pass
    b=iter(list)
    return b
    '''

def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale(iter([1, 5, 2]), 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]
    >>> # generators allow us to represent infinite sequences!!!
    >>> def naturals():
    ...     i = 0
    ...     while True:
    ...         yield i
    ...         i += 1
    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [0, 2, 4, 6, 8]
    """
    "*** YOUR CODE HERE ***"
    try:
        while True:
            yield next(it) * multiplier
    except StopIteration:
        pass


def merge(a, b):
    """Merge two generators that are in increasing order and without duplicates.
    Return a generator that has all elements of both generators in increasing
    order and without duplicates.

    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    "*** YOUR CODE HERE ***"
    try:
        m=next(a)
        n=next(b)
        while True:
            if m<n:
                yield m
                m=next(a)
            elif m>n:
                yield n
                n=next(b)
            else:
                yield m
                m=next(a)
                n=next(b)
    except StopIteration:
        pass


def hailstone(n):
    """Return a generator that outputs the hailstone sequence.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    
    try:
        while True and n>1:
            if n%2==0:
                yield n//2
                n=n//2
                    
            else:
                yield 3*n+1
                n=3*n+1
                    
    except StopIteration:
        pass

