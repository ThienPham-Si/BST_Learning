from Derived_BST import Derived_BST

def main():
    tree = Derived_BST()
    lst = [12,5,46,80,30,2,56,25,10]
    for items in lst:
        tree.insert(items)


    tree.insert(37)
    x = 30
    print(tree.path(x))
    print(tree.parent_node(x))
    print(tree.is_leaf(tree.find_node(x)))
    # print(tree.is_branch(37))
    # print(tree.parent_node(37))

main()
