# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def cost_with_tax(cost, state, tax = 0.05):
    """
    Return total cost given cost, state of purchase, and tax.

    This function takes in the cost of an item, the state of the purchase, 
    and the tax ammount. Tax is defaulted at 0.05. If the state is California,
    tax is set at 0.07. If tax is passed as a percentage, it will be converted
    to a decimal representation of percentage.

    Examples:

    >>> print cost_with_tax(10, 'CA')
    10.7

    >>> print cost_with_tax(20.0, 'TX', 18)
    23.6

    >>> print cost_with_tax(50, 'California', 0.7)
    Please enter State as an abbreviation
    None

    """
    #If tax is entered as whole number, convert to percentage
    if tax >= 1:
        tax = tax/100.0

    #Check whether state entered as abbreviation.
    if len(state) > 2:
        print "Please enter State as an abbreviation"
        return

    if state == "CA":
        tax = 0.07
        
    #Accounts for user error in input type
    try:
        total_cost = cost + (cost * tax)
    except TypeError:
        print "Please enter cost and tax as a number"
        return

    return total_cost

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def is_berry(fruit_name):
    """
    Takes string, returns True/False whether fruit is "strawberry", "cherry", or 
    "blackberry".

    This function takes in a string and returns true if the string is a 
    "strawberry", "cherry", or "blackberry", and False otherwise. Ignores CASE.

    >>> print is_berry("BLACKberry")
    True

    >>> print is_berry("watermelon")
    False

    """
    #Note, doesn't account for if user enters integer. This catch is shown
    #in shipping_cost
    if fruit_name.isalpha():
        return fruit_name.lower() in ["strawberry", "cherry", "blackberry"]
    else:
        print "Please only enter alpha characters"
    

def shipping_cost(fruit_name):
    """
    Take string, returns 0 if fruit is "strawberry", "cherry", or "blackberry", 
    otherwise 5.

    >>> shipping_cost("BLACKberry")
    0

    >>> shipping_cost("watermelon")
    5

    """

    if is_berry(fruit_name):
        return 0
    else:
        return 5


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def is_hometown(town_name):
    """
    Returns boolean of whether town name is 'berkeley'.

    Ignores case.

    Example:
    >>> print is_hometown("BERKELEY")
    True

    >>> print is_hometown("El Cerrito")
    False

    """
    return town_name.lower() == "berkeley"

def full_name(first_name, last_name):
    """
    Inputs first and last name as two strings and returns concatenated string.

    Uses string method title() to print first letter uppercase.

    Example:

    >>> print full_name("maddie", "COusens")
    Maddie Cousens

    """
    return (first_name.title() + " " + last_name.title())

    #Another way to do this would be:
    #return " ".join([first_name.title(), last_name.title()])

def hometown_greeting(town_name, first_name, last_name):
    """
    Takes in three strings, calls town_name and returns string based on boolean.

    This function takes in town name, first and last name, calls function 
    town_name to determine if the town name is the same as the coders home town.
    If True, print's message saying they are from the same place, using
    the full_name function. If False, uses full_name function in print statement
    to ask where user is from


    >>> print hometown_greeting("BERKELEY", "maddie", "cousens")
    Hi, Maddie Cousens, we're from the same place!

    >>> print hometown_greeting("Concord", "Yogi", "Bear")
    Hi Yogi Bear, where are you from?

    """
    if is_hometown(town_name):
        return "Hi, {}, we're from the same place!".format(full_name(first_name, last_name))
    else:
        return "Hi {}, where are you from?".format(full_name(first_name, last_name))



#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def increment(x=1):
    """
    Returns a function object, which contains a copy of the value x, and the 
    function add().

    I believe the function object is called a 'closure'.

    Examples:

    >>> type(increment())
    <type 'function'>

    >>> increment(5)(1)
    6

    """
    def add(y):
        """
        The add function has access to x because it's in scope

        """
        return x + y
    return add

#Create function object addfive
addfive = increment(5)

#Pass 5, 20 as arguments to addfive
addfive(5)
addfive(20)

def number_appending(number, numbers):
    """
    Takes in a number and a list of numbers, appends number to list.

    Example:

    >>> number_appending(5, [1,2,3,4])
    [1, 2, 3, 4, 5]

    >>> number_appending('hi', [1,2,3,4])
    Please enter an number to append

    """
    if type(number) in [int, float]:
        numbers.append(number)
        return numbers
        #NOTE, can't write return numbers.append(number) --> returns None
    else:
        print "Please enter an number to append"
        
    

# Doc Strings Testings
if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"

#####################################################################