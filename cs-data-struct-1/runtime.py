def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Worst case: Same except for last letter. 
    Doing two O(1) operation O(N) times

    Put runtime here:
    -----------------
    [O(n)]


    """

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Worst case: there are no exotic animals
    2 O(n) lookups

    Put runtime here:
    -----------------
    [O(n)]

    """

    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    set(list) O(n)
    2*len(set) O(1) lookups
    O(2n) --> O(n)

    Put runtime here:
    -----------------
    [O(n)]

    """

    result = [] # O(1)

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers) # O(n)

    for x in s: # O(n)
        if -x in s: # O(1)
            result.append([-x, x]) # O(1)

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Worst case: no numbers sum to zero
    Nested for loops: O(n^2) 
    append to list O(1)

    Put runtime here:
    -----------------
    [O(n^2)]

    """

    result = [] # O(1)

    for x in numbers: # O(n)
        for y in numbers: # O(n)
            if x == -y: # O(1)
                result.append((x, y)) # O(1)
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    O(n^2) nested for loops
    O(1) comparison (x == -y)
    O(n) lookup (where n is length of results)
    O(n^2 + n) --> O(n^2) (only keep largest term due to Asymptotic Behavior)

    Put runtime here:
    -----------------
    [O(n^2)]

    """

    result = [] # O(1)

    for x in numbers: # O(n)
        for y in numbers: # O(n)
            if x == -y and (y, x) not in result: # O(1) + # O(n)
                result.append((x, y))
    return result
