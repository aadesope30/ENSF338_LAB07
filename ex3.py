class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.balance = 0


class AVLTree:
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

    def __update_balances(self):
        def height(node):
            if node is None:
                return -1

            left_h = height(node.left)
            right_h = height(node.right)

            node.balance = left_h - right_h
            return 1 + max(left_h, right_h)

        height(self.root)

    def __left_rotate(self, x):
        y = x.right
        if y is None:
            return

        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def __right_rotate(self, x):
        y = x.left
        if y is None:
            return

        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root

        current = self.root
        parent = None
        pivot = None

        
        while current is not None:
            if current.balance != 0:
                pivot = current

            parent = current

            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return current   

        new_node = Node(data, parent)

        if data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node


        # Case 1: no pivot
        if pivot is None:
            print("Case #1: Pivot not detected")
            self.__update_balances()
            return new_node

        # Case 2: pivot exists, inserted into shorter subtree
        if (pivot.balance > 0 and data > pivot.data) or (pivot.balance < 0 and data < pivot.data):
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            self.__update_balances()
            return new_node

        # Case 3: inserted into longer subtree
        # Split into 3a (outside) and 3b (inside)
        if pivot.balance > 0:
            child = pivot.left

            if data < child.data:
                print("Case #3a: adding a node to an outside subtree")
                self.__right_rotate(pivot)
                self.__update_balances()
                return new_node
            else:
                print("Case 3b not supported")
                self.__update_balances()
                return new_node

        else:
            child = pivot.right

            # outside = right-right
            if data > child.data:
                print("Case #3a: adding a node to an outside subtree")
                self.__left_rotate(pivot)
                self.__update_balances()
                return new_node
            else:
                print("Case 3b not supported")
                self.__update_balances()
                return new_node

    def print_inorder_with_balance(self):
        def inorder(node):
            if node is not None:
                inorder(node.left)
                print(f"Node {node.data}, balance = {node.balance}")
                inorder(node.right)

        inorder(self.root)

# -------- Test 1: Case 1 --------
print("TEST 1")
t1 = AVLTree()
for x in [30, 20, 40, 10]:
    t1.insert(x)
t1.print_inorder_with_balance()
print()


# -------- Test 2: Case 2 --------
print("TEST 2")
t2 = AVLTree()
for x in [30, 20, 40]:
    t2.insert(x)
t2.print_inorder_with_balance()
print()


# -------- Test 3: Case 3a --------
print("TEST 3")
t3 = AVLTree()
for x in [30, 20, 10]:
    t3.insert(x)
t3.print_inorder_with_balance()
print()


# -------- Test 4: Case 3b --------
print("TEST 4")
t4 = AVLTree()
for x in [30, 10, 20]:
    t4.insert(x)
t4.print_inorder_with_balance()
print()