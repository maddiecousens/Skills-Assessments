## Recursion ##

# 1. In your own words, what is recursion?

#    Recursion is when a function calls itself. I like to think of it in terms 
#    of dependencies - the answer to the first call is dependent on 
#    the answer to subsequent recursive function calls that ideally break the 
#    problem into smaller chunks as the call stack grows until it reaches a 
#    'base case'. (see next answer for what a base case is). Visually i think of 
#    recursion as a tree - each recursive call creates another branch and once 
#    it hits he base case it begins climbing back up the tree, returning values 
#    until it reaches the original function call. 

# 2. Why is it necessary to have a base case? 

#    A base case stops the recursive function from calling itself and begins 
#    the process of iterating back up the call stack. It is necessary to have 
#    a base case in order for recursion to stop. If there is no base case, the 
#    function will recurse forever, similar to an infinite while loop (in 
#    reality it will error out due to 'stack overflow' - a protection built in 
#    by many programs to stop recursive calls at a certain threshold before 
#    the take up all the computers memory).

## Graphs ##

# 1. What is a graph?

#    A graph is an abstract mathmatical concept that we implement in computer
#    science using Node objects. Essentially a graph is a system of nodes 
#    (sometimes called a vertex or vertices), where each node knows which node 
#    is directly adjacent to it. These adjacent nodes are part of the node's 
#    "adjacency list". Nodes  are connected via an "Edge" (sometimes called 
#    an "Arc"). These Edges can carry "weight", often thought of as the 
#    cost or implications of traveling from one node to the other 
#    (ex: if nodes are cities, weight of an edge could be the price to 
#    fly between cities). Unlike a tree, graphs allow for "cycles" - when a 
#    node can travel edges and arrive back at itself. Graphs can be acyclic 
#    (no cycles) or cyclic (cycles). Some graphs allow flow from node to node 
#    in both directions (non-directed), while some graphs specify a direction 
#    in which you can traverse from node to node (directed).

# 2. How is a graph different from a tree?

#    A graph is different from a tree becaue it can contain cycles and can be
#    non-directed. Trees are directed, acyclic graphs (Therefore a tree is a 
#    graph but a graph is not always a tree). Tree's cannot have cycles.
#    Some good ways to tell that something is a graph instead of a tree:
#       - if there are multiple ways of getting to a node
#       - if a node has more than one parent

# 3. Give an example of something that would be good to model with a graph.
#    A network of frienships could be modeled using a graph. Each edge 
#    indicates a friendship (perhaps it could have a weight of how many 
#    years two people(nodes) have been friends). The graph would be 
#    non-directed and contain cycles because you can be friends through 
#    many different people.











