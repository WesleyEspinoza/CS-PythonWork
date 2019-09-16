from set_hashtable import HashTable

class CustomSet(object):

    def __init__(self, elements=[]):
        self.hashTable = HashTable()
        self.size = 0
        for item in elements:
            self.add(item)


    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}'.format(val) for val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'set({!r})'.format(self.items())

    def __iter__(self):
        pass

    def add(self, value):
        self.hashTable.set(value)
        self.size += 1

    def remove(self, value):
        self.hashTable.delete(value)
        self.size -= 1

    def contains(self, value):
        return self.hashTable.contains(value)

    def items(self):
        return self.hashTable.items()

    def length(self):
         return self.hashTable.length()

    def union(self, other_set):
        other_set_items = other_set.items()
        set_items = self.items()
        new_set = CustomSet()
        for item in other_set_items:
            new_set.add(item)
        for item in set_items:
            new_set.add(item)
        return new_set

    def intersection(self, other_set):
        new_set = CustomSet()
        if other_set.length() > self.length():
            for item in other_set.items():
                if self.contains(item):
                    new_set.add(item)
        else:
            for item in self.items():
                if other_set.contains(item):
                    new_set.add(item)
        return new_set


    def is_subset(self, other_set):
        if other_set.size > self.size:
            return False
        else:
            for item in other_set.items():
                if self.contains(item) == False:
                    return False
            return True

    def difference(self, other_set):
        new_set = CustomSet()
        for item in self.items():
            if other_set.contains(item) == False:
                new_set.add(item)
        return new_set

if __name__ == '__main__':
    print(CustomSet([1,2,3]))
