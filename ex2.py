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

    def compute_balances(self):
        def height(node):
            if node is None:
                return -1

            left_h = height(node.left)
            right_h = height(node.right)

            node.balance = left_h - right_h
            return 1 + max(left_h, right_h)

        height(self.root)

    def insert(self, data):
        # empty tree
        if self.root is None:
            self.root = Node(data)
            self.compute_balances()
            print(f"Inserted root node {data}")
            return self.root

        current = self.root
        parent = None
        pivot = None

        # find insertion position and deepest pivot on the path
        while current is not None:
            if current.balance != 0:
                pivot = current

            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        # insert new node
        new_node = Node(data, parent)
        if data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        # case detection
        if pivot is None:
            print("Case #1: Pivot not detected")

        else:
            inserted_in_left_subtree = data < pivot.data

            # Case 2: pivot exists, but insertion is into shorter subtree
            if (pivot.balance > 0 and not inserted_in_left_subtree) or \
               (pivot.balance < 0 and inserted_in_left_subtree):
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")

            else:
                # inserted into longer subtree -> Case 3 or Case 4
                if inserted_in_left_subtree:
                    child = pivot.left
                    if data < child.data:
                        print("Case 3 not supported")
                    else:
                        print("Case 4 not supported")
                else:
                    child = pivot.right
                    if data > child.data:
                        print("Case 3 not supported")
                    else:
                        print("Case 4 not supported")

        # always recompute balances so stored balances stay correct
        self.compute_balances()
        return new_node

    def print_inorder_with_balance(self):
        def inorder(node):
            if node is not None:
                inorder(node.left)
                print(f"Node {node.data}, balance = {node.balance}")
                inorder(node.right)
        inorder(self.root)


# ---------------- TEST 1: Case 1 ----------------
print("TEST 1")
t1 = BinarySearchTree()
t1.insert(30)
t1.insert(20)
t1.insert(40)
t1.insert(10)   # Case #1: Pivot not detected
t1.print_inorder_with_balance()
print()


# ---------------- TEST 2: Case 2 ----------------
print("TEST 2")
t2 = BinarySearchTree()
t2.insert(30)
t2.insert(20)
t2.insert(40)   # Case #2: pivot exists, inserted into shorter subtree
t2.print_inorder_with_balance()
print()


# ---------------- TEST 3: Case 3 ----------------
print("TEST 3")
t3 = BinarySearchTree()
t3.insert(30)
t3.insert(20)
t3.insert(10)   # Case 3 not supported
t3.print_inorder_with_balance()
print()


# ---------------- TEST 4: Case 4 ----------------
print("TEST 4")
t4 = BinarySearchTree()
t4.insert(30)
t4.insert(10)
t4.insert(20)   # Case 4 not supported
t4.print_inorder_with_balance()
print()