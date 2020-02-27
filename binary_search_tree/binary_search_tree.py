from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')

"""
PLAN

Use recursion
Steps - Iteratively or Recursively

- Starting at the root
    - Check if there is a root. If not, the root becomes that new node!
    - If there is a root, check if the value of the new node is greater than or less than the value of the root
    - **If it is less**
        - Check to see if there's a node to the left
            - If there is, move that node and repeat these steps
            - If there is not, add that node as the left property
    - **If it is greater**
        - Check to see if there's a node to the right
            - If there is, move to that node and repeat these steps
            - If there is not, add that ndoe as the right property
"""


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # print("\ninserting value:", value)
        # print("\nstarting values:", "val:", self.value,
        #       "left:", self.left, "right:", self.right)

        # # If value is the same as the root, return undefined
        # if value == self.value:
        #     return None

        bst = BinarySearchTree(value)
        # If value is less than self.value
        if value < self.value:
            # Is there a node to the left?
            if self.left is None:
                self.left = bst
            else:
                # If so, recurse
                self.left.insert(value)
        # If value is greater than self.value
        else:
            # Is there a node to the right?
            if self.right is None:
                # If not, add that node as the left property
                self.right = bst
            else:
                # If so, recurse
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        if self.left is None and self.right is None:
            return False
        if target < self.value:
            return self.left.contains(target)
        else:
            return self.right.contains(target)
    # Return the maximum value found in the tree

    def get_max(self):
        # If there's nothing to the right, return self.value
        if self.right is None:
            return self.value
        #Else, recurse
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.print_values()
# bst.in_order_print(bst)
print("\nContains :", bst.contains(4))  # true
