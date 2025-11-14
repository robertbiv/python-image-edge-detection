# Binary Search Tree Implementation

A Python implementation of a Binary Search Tree (BST) with support for duplicate keys and advanced operations.

## Description

This project implements a Binary Search Tree data structure with several key features:
- Support for duplicate keys using a count field
- Efficient subtree size tracking
- K-th largest element retrieval
- Standard BST operations (insert, delete, search)

## Features

- **Insert**: Add keys to the tree with automatic duplicate handling
- **Delete**: Remove keys while maintaining tree structure
- **Search**: Find nodes by key value
- **K-th Largest**: Efficiently find the k-th largest key in O(log n) time
- **Subtree Size Tracking**: Each node maintains the count of keys in its subtree

## How to Run

```bash
python3 RobertBennethumPS5.py
```

## Code Structure

### Classes

- **BSTNode**: Represents a node in the binary search tree
  - `key`: The value stored in the node
  - `count`: Number of duplicates of this key
  - `subtree_keys_inclusive`: Total number of keys in this subtree (including duplicates)
  - `left`: Reference to left child
  - `right`: Reference to right child

### Functions

- `insert_bst(node, key)`: Insert a key into the tree
- `delete_bst(node, key)`: Delete a key from the tree
- `search(node, key)`: Search for a key in the tree
- `kth_largest_key(node, k)`: Find the k-th largest key
- `find_min(node)`: Find the minimum key in the tree
- `print_bst(node)`: Print the tree in-order with node details
- `update_subtree_keys_inclusive(node)`: Update the subtree size after modifications

## Example Usage

The code includes a demonstration that:
1. Creates a BST with values: [13, 7, 5, 11, 17, 11, 19, 11]
2. Deletes the key 17
3. Finds the minimum key
4. Searches for specific keys
5. Finds the k-th largest keys (for k = 1 to 8)

## Example Output

```
Minimum: 5
Search for 11: <__main__.BSTNode object at 0x...>
Search for 17: None
Tree:
5 (count: 1, subtree_keys_inclusive: 1)
7 (count: 1, subtree_keys_inclusive: 5)
11 (count: 3, subtree_keys_inclusive: 3)
13 (count: 1, subtree_keys_inclusive: 7)
19 (count: 1, subtree_keys_inclusive: 1)


The 1-th largest key is: 19
The 2-th largest key is: 13
The 3-th largest key is: 11
The 4-th largest key is: 11
The 5-th largest key is: 11
The 6-th largest key is: 7
The 7-th largest key is: 5
The 8-th largest key is: None
```

## Technical Details

### Duplicate Key Handling
Instead of storing multiple nodes for duplicate keys, each node maintains a `count` field. When inserting a duplicate, the count is incremented. When deleting, the count is decremented, and the node is only removed when count reaches zero.

### K-th Largest Algorithm
The k-th largest element is found efficiently by:
1. Checking the size of the right subtree
2. If right subtree has >= k elements, recurse right
3. If right subtree + current node count >= k, return current key
4. Otherwise, recurse left with adjusted k value

This achieves O(log n) time complexity on balanced trees.

## Requirements

- Python 3.x

## Author

Robert Bennethum IV
