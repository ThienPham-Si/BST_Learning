from Derived_BST import Derived_BST

def main():
    tree = Derived_BST()
    lst = [12, 5, 46, 80, 30, 2, 56, 25, 10]

    for items in lst:
        tree.insert(items)

    print('Max value:', tree.get_max())
    print('Min value:', tree.get_min())

    print()
    item_x = int(input('Add an element: '))
    tree.insert(item_x)
    print(f'New node {item_x} has been added to the tree.')
    print(f'{item_x} is a leaf node?', tree.is_leaf(tree.find_node(item_x)))
    print(f'{item_x} is a branch?', tree.is_branch(tree.find_node(item_x)))
    print(tree.parent_node(item_x).value, 'is the parent node of', item_x)

    print()
    print('Total leaf nodes:', tree.total_leaf_nodes_iterative())
    print('Total non-leaf nodes:', tree.total_nonleaf_nodes())

    print()
    print('Breath-First Traversal')
    tree.breadth_first()

main()
