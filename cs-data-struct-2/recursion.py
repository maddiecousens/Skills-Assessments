# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """
    if not my_list:
        return

    print my_list[i]
    print_item(my_list[1:])

# Another way (less recursive-y since doesn't reduce problem size)

    # if i == len(my_list):
    #     return
    # print my_list[i]
    # print_item(my_list, i + 1)

# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """
    # set current_node to tree for clarity
    current_node = tree
    # print current node
    print current_node.data
    # recursively call function for every child node
    for child in current_node.children:
        print_all_tree_data(child)

# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """
    # if list is empty, return zero
    if not my_list:
        return 0
    # otherwise return 1 + recursive call
    return 1 + list_length(my_list[1:])


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
        >>> four = Node(4)
        >>> five = Node(5)
        >>> two.add_child(four)
        >>> two.add_child(five)
        >>> num_nodes(one)
        5
        >>> six = Node(6)
        >>> three.add_child(six)
        >>> num_nodes(one)
        6
    """
    # set current node to tree for clarity
    current_node = tree
    count = 1
    # for ever child node make a recursive call. If leaf node, function returns 1
    for child in current_node.children:
        count += num_nodes(child)
    return count


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
