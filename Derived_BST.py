from bst import BST


class Derived_BST(BST):
    def __init__(self):
        super().__init__()

    @staticmethod
    def is_leaf(node):
        if node.left is None and node.right is None:
            return True
        return False

    @staticmethod
    def is_branch(node):
        if node.left is not None and node.right is not None:
            return True
        return False

    def find_node(self, value):
        current = self.root
        while current:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return current

    def parent_node(self, value):
        current = self.root
        parent = None
        while current:
            if value >= current.value:
                if current.value == value:
                    if parent is None:
                        return None
                    return parent
                else:
                    parent = current
                    current = current.right
            else:
                parent = current
                current = current.left

        print(f"The value {value} does not exist in the tree")
        return

    # Since this is a BST, the right child must be bigger than parent, keep checking if the current pointer
    # has a right child, if it has then set the current pointer to that child and repeat, if the current pointer
    # doesn't have a right child it's the biggest value
    def get_max(self):
        current = self.root
        while current.right:
            current = current.right

        return current.value

    # Same idea with get_max
    def get_min(self):
        current = self.root
        while current.left:
            current = current.left

        return current.value

    def total_leaf_nodes(self, node):
        if node is None:
            return 0

        if self.is_leaf(node):
            return 1
        else:
            return self.total_leaf_nodes(node.left) + self.total_leaf_nodes(node.right)

    def total_leaf_nodes_iterative(self):
        stack = list()
        stack.append(self.root)
        count = 0
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if self.is_leaf(node):
                count += 1

        return count

    def total_nonleaf_nodes(self):
        stack = list()
        stack.append(self.root)
        count = 0
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if not self.is_leaf(node):
                count += 1

        return count

    def breadth_first(self):
        queue_lst = list()
        queue_lst.append(self.root)
        display_lst = list()
        while queue_lst:
            node = queue_lst.pop(0)
            if node.left:
                queue_lst.append(node.left)
            if node.right:
                queue_lst.append(node.right)
            display_lst.append(node.value)

        return self.display_breadth(display_lst)

    # This is a simple code to display a well-balanced breadth_first tree
    @staticmethod
    def display_breadth(display_lst):
        power = 0
        while display_lst:
            count = 2 ** power
            for i in range(count):
                try:
                    pop_item = display_lst.pop(0)
                except IndexError:
                    break
                print(pop_item, end=' ')
            power += 1
            print()
