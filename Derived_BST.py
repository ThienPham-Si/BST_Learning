from bst import BST

class Derived_BST(BST):
    def __init__(self):
        super().__init__()

    def is_leaf(self, node):
        if node.left == None and node.right == None:
            return True
        return False

    def is_branch(self, node):
        if node.left != None and node.right != None:
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
                    if parent == None:
                        return None
                    return parent.value
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

    # def breadth_first(self):
    #     return self.bf_helper(self.root)
    #
    # def bf_helper(self, node):
    #     queue_lst = []
    #     queue_lst.append(node.val)
    #     if node.left != None:
    #         return self.bf_helper(node.left)
    #     if



