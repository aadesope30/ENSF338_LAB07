import random
import time
import matplotlib.pyplot as plt



#Implementation of BST with Insertion and Search Operations
class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.balance = 0 


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        new_node = Node(data, parent)

        if data <= parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        return new_node

    
    def search(self, data):
        current = self.root

        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return None

    # Question 2: compute balance for each node
    def compute_balances(self):
        def helper(node):
            if node is None:
                return -1   # height of empty subtree

            left_height = helper(node.left)
            right_height = helper(node.right)

            node.balance = left_height - right_height
            return 1 + max(left_height, right_height)

        helper(self.root)

    def max_absolute_balance(self):
        max_balance = 0

        def traverse(node):
            nonlocal max_balance
            if node is None:
                return

            abs_balance = abs(node.balance)
            if abs_balance > max_balance:
                max_balance = abs_balance

            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return max_balance


NUM_VALUES = 1000
NUM_TASKS = 1000

values = list(range(1, NUM_VALUES + 1))

x_balances = []
y_times = []

for _ in range(NUM_TASKS):
    task = values[:]
    random.shuffle(task)

    bst = BinarySearchTree()
    for value in task:
        bst.insert(value)

    
    bst.compute_balances()
    largest_abs_balance = bst.max_absolute_balance()

    start = time.perf_counter()

    for value in values:
        bst.search(value)

    end = time.perf_counter()

    total_search_time = end - start
    average_search_time = total_search_time / NUM_VALUES

    x_balances.append(largest_abs_balance)
    y_times.append(average_search_time)


# Part 5: scatterplot
plt.scatter(x_balances, y_times)
plt.xlabel("Largest Absolute Balance")
plt.ylabel("Average Search Time (seconds)")
plt.title("BST Balance vs Search Time")
plt.savefig("Ex5.png", dpi=300, bbox_inches="tight")
plt.show()