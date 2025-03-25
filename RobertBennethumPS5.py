#Robert Bennethum IV
#CMPSC 462
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.subtree_keys_inclusive = 1
        self.left = None
        self.right = None

def update_subtree_keys_inclusive(node):
    if node is not None:
        node.subtree_keys_inclusive = node.count + (node.left.subtree_keys_inclusive if node.left else 0) + (node.right.subtree_keys_inclusive if node.right else 0)

def insert_bst(node, key):
    if node is None:
        return BSTNode(key)

    if key < node.key:
        node.left = insert_bst(node.left, key)
    elif key > node.key:
        node.right = insert_bst(node.right, key)
    else:
        node.count += 1
    update_subtree_keys_inclusive(node)
    return node

def delete_bst(node, key):
    if node is None:
        return node
    if key < node.key:
        node.left = delete_bst(node.left, key)
    elif key > node.key:
        node.right = delete_bst(node.right, key)
    else:
        if node.count > 1:
            node.count -= 1
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            successor = find_min(node.right)
            node.key = successor.key
            node.count = successor.count
            node.right = delete_bst(node.right, successor.key)
    update_subtree_keys_inclusive(node)
    return node

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def print_bst(node):
    if node is not None:
        print_bst(node.left)
        print(f"{node.key} (count: {node.count}, subtree_keys_inclusive: {node.subtree_keys_inclusive})")
        print_bst(node.right)

def search(node, key):
    if node is None:
        return None
    if key < node.key:
        return search(node.left, key)
    elif key > node.key:
        return search(node.right, key)
    else:
        return node

def kth_largest_key(node, k):
    if node is None:
        return None
    right_subtree_keys_inclusive = node.right.subtree_keys_inclusive if node.right else 0
    if right_subtree_keys_inclusive >= k:
        return kth_largest_key(node.right, k)
    elif right_subtree_keys_inclusive + node.count >= k:
        return node.key
    else:
        return kth_largest_key(node.left, k - right_subtree_keys_inclusive - node.count)

# Recreate the tree from the example figure
root = None
for i in [13, 7, 5, 11, 17, 11, 19, 11]:
    root = insert_bst(root, i)
root = delete_bst(root, 17)
print("Minimum:", find_min(root).key)
print("Search for 11:", search(root, 11))
print("Search for 17:", search(root, 17))
print("Tree:")
print_bst(root)
print("\n")
# Find the k-th largest key
for k in range(1, 9):
    print(f"The {k}-th largest key is:", kth_largest_key(root, k))