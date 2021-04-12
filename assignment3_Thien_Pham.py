from Derived_BST import Derived_BST

def main():
    tree = Derived_BST()
    lst = [12, 5, 46, 80, 30, 2, 56, 25, 10, 99]

    lst_2 = [1, 2, 3, 4, 5, 6, 7]
    tree_2 = Derived_BST()
    for items in lst_2:
        tree_2.insert(items)

    for items in lst:
        tree.insert(items)

    tree_2.breadth_first()
    print(tree_2.total_leaf_nodes_iterative())
    print(tree_2.total_leaf_nodes(tree_2.get_root()))
    print(tree_2.total_nonleaf_nodes())

main()
