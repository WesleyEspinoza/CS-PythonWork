from queue import Queue

class BinaryTreeNode(object):
#log2n where n is items
    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.depth = 0

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        if self.right == None and self.left == None:
            return True
        return False

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        if self.is_leaf():
            return False
        return True

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""

        if self.left != None and self.right != None:
            left = self.left
            right = self.right
            left_height = left.height()
            right_height = right.height()
            max_height = max(left_height, right_height)
            return max_height + 1
        elif self.left != None:
            node = self.left
            return node.height() + 1
        elif self.right != None:
            node = self.right
            return node.height() + 1
        else:
            return 0

    def node_depth(self):
        """Returns the level that the node is on"""
        return self.depth



class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        # TODO: Check if root node has a value and if so calculate its height
        if self.root.data != None:
            return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item, node = None):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # TODO: Return the node's data if found, or None
        if node == None:
            return None

        if node.data == item:
            return node.data
        elif node.data > item:
            return search(item, node.left)
        elif node.data < item:
            return search(item, node.right)

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # TODO: Create a new root node
            self.root = BinaryTreeNode(item)
            # TODO: Increase the tree size
            self.size +=1
            return
        # Find the parent node of where the given item should be inserted
        new_node = BinaryTreeNode(item)
        parent = self.root
    # TODO: Check if the given item should be inserted left of parent node

    #get to a leaf node before continuing
        while parent.left != None and parent.right != None:
            if parent.data > item:
                parent = parent.left
            else:
                parent = parent.right

        if parent.data > item:
            if parent.left == None:
                parent.left = new_node
            else:
                left_node = parent.left
                if left_node.data >= item:
                    new_node.left = parent.left
                    new_node.right = parent.right
                else:
                    new_node.right = parent.left
                    new_node.left = parent.right
                parent.left = new_node
        else:
            if parent.right == None:
                parent.right = new_node
            else:
                right_node = parent.right
                if right_node.data >= item:
                    new_node.right = parent.right
                    new_node.left = parent.left
                else:
                    new_node.right = parent.left
                    new_node.left = parent.right
                parent.right = new_node

        new_node.parent = parent
        new_node.depth = parent.depth+1
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if ...:
                # Return the found node
                return node
            # TODO: Check if the given item is less than the node's data
            elif ...:
                # TODO: Descend to the node's left child
                node = ...
            # TODO: Check if the given item is greater than the node's data
            elif ...:
                # TODO: Descend to the node's right child
                node = ...
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        elif node.data == item:
            # Return the found node
            return node
        # TODO: Check if the given item is less than the node's data
        elif node.data > item:
            # TODO: Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # TODO: Check if the given item is greater than the node's data
        elif node.data < item:
            # TODO: Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if ...:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            elif ...:
                # TODO: Update the parent and descend to the node's left child
                parent = ...
                node = ...
            # TODO: Check if the given item is greater than the node's data
            elif ...:
                # TODO: Update the parent and descend to the node's right child
                parent = ...
                node = ...
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # if node is None:
        #     # Not found (base case)
        #     return None
        # elif node.data == item:
        #     # Return the found node
        #     return node.parent
        # elif node.data > item:
        #     return self._find_parent_node_recursive(item, node.left)
        # # TODO: Check if the given item is greater than the node's data
        # elif node.data < item:
        #     # TODO: Recursively descend to the node's right child, if it exists
        #     return self._find_parent_node_recursive(item, node.right)

        return(_find_node_recursive(item,self.root).parent)



    def delete(self, item, root):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""

        if not root:
            return root

        if root.data > item:
            root.left = self.delete(item,root.left)
        elif root.data < item:
            root.right = self.delete(item, root.right)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp_value = root.right
            min_value = temp_value.data

            while temp_value.left:
                temp_value = temp_value.left
                min_value = temp_value.data

            root.data = min_value
            root.right = self.delete(root.data, root.right)

        return root







    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node:
            self._traverse_in_order_recursive(node.left, visit)
            visit(node.data)
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""

        # Variables and pointers to keep track of nodes and status as we traverse
        current_node = node
        stack = LinkedStack()
        done = False

        while not done:
            if current_node is not done:
                stack.push(current_node)
                current_node = current_node.left
            else:
                if not stack.is_empty():
                    current_node = stack.pop()
                    visit(current_node)
                    current_node = current_node.right
                else:
                    done = True

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        visit(node.data)
        if node.left:
            self._traverse_pre_order_recursive(node.left, visit)

        if node.right:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""

        if node.left:
            self._traverse_post_order_recursive(node.left, visit)

        if node.right:
            self._traverse_post_order_recursive(node.right, visit)

        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        q = Queue()
        q.enqueue(start_node)
        while not q.is_empty():
            node = q.dequeue()
            visit(node.data)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
