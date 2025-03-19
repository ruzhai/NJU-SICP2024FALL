""" Homework 5: Nonlocal and Generators"""

from ADT import tree, label, branches, is_leaf, print_tree

#####################
# Required Problems #
#####################


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    attempts = []
    def withdraw(amount, pw):
        if pw == password and len(attempts) < 3:
            nonlocal balance
            if amount > balance:
                return 'Insufficient funds'
            balance -= amount
            return balance
        else:
            
            if len(attempts) == 3:
                return "Your account is locked. Attempts: " + str(attempts)
            else:
                attempts.append(pw)
                return 'Incorrect password'
    return withdraw



def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    if withdraw(0, old_pass) == "Incorrect password":
        return "Incorrect password"
    elif type(withdraw(0, old_pass)) is int:
        def inner_withdraw(amount, pw):
            if pw == old_pass:
                return withdraw(amount, old_pass)
            elif pw == new_pass:
                return withdraw(amount, old_pass)
            else:
                return withdraw(amount, pw)
        return inner_withdraw
    else:
        return withdraw(0, new_pass)

def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of all elements in seq. The permutations could be yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    seq = list(seq)
    if len(seq) == 1:
        yield [seq[0]]
    else:   
        list1 = []
        for i in range(len(seq)):
            flag = 1
            for item in range(len(list1)):
                if list1[item] == seq[i]:
                    flag = 0
            if flag == 0:
                continue
            list1.append(seq[i])
            
            for perm in permutations(seq[:i] + seq[i+1:]):
                
                yield [seq[i]] + perm
    '''
    seq = list(seq)
    if len(seq) == 1:
        yield [seq[0]]
    else:   
        for i in range(len(seq)):
            f = lambda x, i=i: x[i]
            g = lambda x, i=i: x[:i] + x[i+1:]
            for perm in permutations(g(seq)):
                
                yield [f(seq)] + perm
    '''
    '''
    if len(seq) == 1:
        yield [seq[0]]
    else:   
        for i in range(len(seq)):
            
            for perm in permutations(seq[:i] + seq[i+1:]):
                
                yield [seq[i]] + perm
   '''
   

    
    '''
    if len(seq) == 1:  
        yield [seq[0]]
    else:
        for perm in permutations(seq[1:]):
            for i in range(len(seq)):
                yield perm[:i] + [seq[0]] + perm[i:]
    '''

def two_sum_pairs(target, pairs):
    """Return True if there is a pair in pairs that sum to target."""
    for i, j in pairs:
        if i + j == target:
            return True
    return False


def pairs(lst):
    """Yield the search space for two_sum_pairs.

    >>> two_sum_pairs(1, pairs([1, 3, 3, 4, 4]))
    False
    >>> two_sum_pairs(8, pairs([1, 3, 3, 4, 4]))
    True
    >>> lst = [1, 3, 3, 4, 4]
    >>> plst = pairs(lst)
    >>> n, pn = len(lst), len(list(plst))
    >>> n * (n - 1) / 2 == pn
    True
    """
    "*** YOUR CODE HERE ***"
    
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            yield (lst[i], lst[j])


def two_sum_list(target, lst):
    """Return True if there are two different elements in lst that sum to target.

    >>> two_sum_list(1, [1, 3, 3, 4, 4])
    False
    >>> two_sum_list(8, [1, 3, 3, 4, 4])
    True
    """
    visited = []
    for val in lst:
        "*** YOUR CODE HERE ***"
        
        if val in visited:
            return True
        visited.append(target - val)

    return False


def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.
    >>> k = tree(5, [tree(7, [tree(2)]), tree(8, [tree(3), tree(4)]), tree(5, [tree(4), tree(2)])])
    >>> v = tree('Go', [tree('C', [tree('C')]), tree('A', [tree('S'), tree(6)]), tree('L', [tree(1), tree('A')])])
    >>> type(lookups(k, 4))
    <class 'generator'>
    >>> sorted([f(v) for f in lookups(k, 2)])
    ['A', 'C']
    >>> sorted([f(v) for f in lookups(k, 3)])
    ['S']
    >>> [f(v) for f in lookups(k, 6)]
    []
    """
    "*** YOUR CODE HERE ***"
    '''
    def list_lookup(node):
        list = []
        list.append(label(node))
        for branch in branches(node):
            if is_leaf(branch):
                list.append(label(branch))
            else:
                list.extend(list_lookup(branch))
        return list
    '''
    def list_lookup(node):
        return sum([list_lookup(branch) for branch in branches(node)], [label(node)])
    a=list_lookup(k)
    for i in range(len(a)):
        if a[i]==key:
            yield (lambda x: list_lookup(x)[i])




##########################
# Just for fun Questions #
##########################


def remainders_generator(m):
    """Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    0
    4
    8
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"


def starting_from(start):
    """Yields natural numbers starting from start.

    >>> sf = starting_from(0)
    >>> [next(sf) for _ in range(10)] == list(range(10))
    True
    """
    "*** YOUR CODE HERE ***"


def sieve(t):
    """Suppose the smallest number from t is p, sieves out all the
    numbers that can be divided by p (except p itself) and recursively
    sieves out all the multiples of the next smallest number from the
    reset of of the sequence.

    >>> list(sieve(iter([3, 4, 5, 6, 7, 8, 9])))
    [3, 4, 5, 7]
    >>> list(sieve(iter([2, 3, 4, 5, 6, 7, 8])))
    [2, 3, 5, 7]
    >>> list(sieve(iter([1, 2, 3, 4, 5])))
    [1]
    """
    "*** YOUR CODE HERE ***"

def primes():
    """Yields all the prime numbers.

    >>> p = primes()
    >>> [next(p) for _ in range(10)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    "*** YOUR CODE HERE ***"
