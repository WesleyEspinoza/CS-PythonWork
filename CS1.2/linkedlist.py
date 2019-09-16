#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0 # length of LL
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(1) Why and under what conditions?
        because it only returns teh size and nothing else
        """
        # TODO: Loop through all nodes and count one for each
        return self.size


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?
        this example would be O1 because it does not go into any loops
        """
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        self.size += 1
        current = self.head
        node = Node(item)
        if current:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node



    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?
        this example would be O1 because it does not go into any loops
        """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        self.size += 1
        new_node = Node(item)
        if not self.is_empty():
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def replace(self, item, value, all_nodes = False):
        """Finds and replaces a value in the linked list"""
        node = self.head
        previous_node = None
        while node is not None:
            if node.data == item:
                new_node = Node(value)
                new_node.next = node.next
                if node == self.head:
                    self.head = new_node
                if node == self.tail:
                    self.tail = new_node
                if previous_node is not None:
                    previous_node.next = new_node
                if not all_nodes:
                    break
            previous_node = node
            node = node.next

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) Why and under what conditions?
            because if the node is the first object the results would not be dependent on the length of the list

        TODO: Worst case running time: O(n) Why and under what conditions?
            this would be the worst case because if the element is  the last on the list is has to go through the whole list.
        """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        item = self.head
        while item is not None:
            if quality(item.data):
                return item.data
            item = item.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Why and under what conditions?
    because if the node is the first object the results would not be dependent on the length of the list

        TODO: Worst case running time: O(n) Why and under what conditions?
        this would be the worst case because if the element is  the last on the list is has to go through the whole list.
        """
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
         # Store head node
        self.size -= 1

        node = self.head
        previous_node = None
        next_node = None

        item_found = False

        while node is not None:
            next_node = node.next
            if node.data == item:
                item_found = True
                if previous_node is not None:
                    if node == self.tail:
                        self.tail = previous_node
                        self.tail.next = None
                    else:
                        previous_node.next = next_node
                elif node == self.head:
                    self.head = next_node
                    if next_node is None:
                        self.tail = None

            if not item_found:
                previous_node = node
                node = node.next
            else:
                node = None

        if not item_found:
            raise ValueError('Item not found: {}'.format(item))



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
