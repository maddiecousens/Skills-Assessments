discussion questions

Runtime

1. Assuming there is absolutely no sorting and pulling a cracker is random, pulling a cracker would scale at O(n), where n is the number of crackers in your box. The worst case scenario is that there is NO elephant at all, and you have to look at every cracker.

2. O(1), O(log n), O(n log n), O(n^2), O(2^n)

Stacks and Queues
1.1 A stack. This is a LIFO situation. The last pallet you load, will be the first pallet you pull out when unloading.

1.2 A queue. This is a FIFO situation. The first bottle to be loaded on the assembly line will be the first bottle to receive a cap.

1.3 
This is best solved using stacks. You can use a stack to adjust the equation into a more computer readable form called postfix notation: 2 7 4 * + 3 2 / +

(When you encounter a operand, push to output, when you encounter an operator or a parenthesis, push to stack if it has higher priority than top stack item. If the operand has a lower or equal priority than the top stack item, pop the stack and add to output until you operand has higher priority - then add to stack. To handle parenthesis: Left parenthesis should have higher priority than any other symbol, thus you add it to the stack and only pop if you encounter a right parenthesis. example below)

2 + (7 * 4) - (3 / 2)
2 #push to output output = 2 | stack = []
+ #push to stack. output = 2 | stack = [+]
( #push to stack. output = 2 | stack = [+,(]
7 #push to output output = 2 7 | stack = [+,(]
* #push to stack (lower priority than left parenth) output = 2 7| stack = [+,(,*]
4 #push to output. output = 2 7 4 | stack = [+,(,*]
) #pop stack until find left parenth , pop left parenth, don't add to output. output = 2 7 4 * | stack = [+]
- #pop stack becuas - is equal priority to +. push -. output = 2 7 4 * + | stack = [-]
( #push to stack. output = 2 7 4 * + | stack = [-, (]
3 #push to output. output = 2 7 4 * + 3| stack = [-, (]
/ #push to stack since lower priority than left parenth. output = 2 7 4 * + 3| stack = [-, (, /]
2 #push to output. output = 2 7 4 * + 3 2 | stack = [-, (, /]
) #pop until left parenth. output = 2 7 4 * + 3 2 /| stack = [-]
  #pop remaining stack. output = 2 7 4 * + 3 2 / -


Then use an additional stack to compute the expression. If you encounter an integer, push it to the stack. When you encounter and operand, pop two off the stack, compute using the operand and push the result back onto the stack. 

2.a Queues are appropriate data structures when doing a breadth first search on a tree- when you encounter a node, you enqueue it's children at the end of the line, but you still process the nodes in FIFO order - dequeuing from the front.

2.b Queues are the appropriate data structure when you want to process items in the order in which you received them - for example, a printer will print the first task it receives, however while it's printing that other tasks can enqueue. It will process these tasks in FIFO order. 

3.a Stacks are appropriate data structures whenever you are backtracking, an example of this is an undo button - you undo the most recent action you took. This is LIFO order.

3.b Another use of a stack is in a call stack. When you recurse, every function is added to the stack. When it reaches the base case it begins popping from the stack (i.e LIFO) and tracing back to the beginning. Even non-recursive calls are stored in a stack - this is why you see a trace back when something errors out- it gives you the most recent call, then the call that called that call, etc. 

Linked Lists
1. 
Nodes: 
    apple_node, berry_node, cherry_node
Data:
    apple_node.data = "Apple"
    berry_node.data = "Berry"
    cherry_node.data = "Cherry"
Head:
    apple_node
Tail:
    there is no tail in this diagram
Other attributes:
    head.next = apple_node
    apple_node.next = berry_node
    berry_node.next = cherry_node
    cherry_node.next = None

2.
In a singly-linked list, every node only has one pointer, pointing to it's next node. In a doubly-linked list each node has two pointers, one pointing to the previous node and one pointing to the next node.

### ADD more on the benefits of each.

3. It is easier to append to a linked list with a tail because linked lists do not have indexes, therefore without a tail we have to walk through each node beginning at the head until node.next is None. This scales terribly at O(n)

Trees

1. food, Italian, indian, Mexican, lasagna, pizza, tikka masala, saag, burrito
2. food, Mexican, enchiladas, taco, burrito
indian, saag,tikka masala, Italian, pizza, Sicilian, New York-style, CHICAGO STYLE!

### double check

3. A binary tree is a tree where each node has 0 to 2 children. A binary SEARCH tree is a binary tree that has the ordering property that all left descendants have values less than it's parent node and all right descendants have values greater than it's parent node. This must be true for all nodes. If the tree is balanced, the runtime scales at O(log n). However, if the tree is not balanced the runtime scales at O(n).



