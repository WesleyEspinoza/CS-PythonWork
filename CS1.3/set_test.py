#!python

from set import CustomSet
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        s = CustomSet()
        assert s.size == 0
        assert s.length() == 0

    def test_init_with_list(self):
        s = CustomSet(['a','b','c'])
        assert s.length() == 3

    def test_length_add(self):
        s = CustomSet()
        s.add('a')
        s.add('b')
        s.add('c')
        assert s.length() == 3
        assert s.size == 3

    def test_delete(self):
        s = CustomSet()
        s.add('a')
        s.add('b')
        s.add('cee')
        s.remove('cee')
        assert s.length() == 2
        assert s.size == 2

    def test_contains(self):
        s = CustomSet()
        s.add('a')
        s.add('b')
        s.add('c')
        assert s.contains('a') == True
        assert s.contains('z') == False


    def test_union(self):
        s = CustomSet()
        d = CustomSet()
        s.add('a')
        s.add('b')
        s.add('c')
        s.remove('c')
        d.add('c')
        d.add('d')
        d.add('e')
        d.add('f')

        n = s.union(d)
        assert n.contains('a') == True
        assert n.contains('b') == True
        assert n.contains('c') == True
        assert n.contains('d') == True
        assert n.contains('e') == True
        assert n.contains('f') == True

        assert n.length() == 6
        assert n.size == 6

    def test_intersection(self):
        s = CustomSet()
        d = CustomSet()
        s.add('a')
        s.add('b')
        s.add('c')
        d.add('c')
        d.add('d')
        d.add('e')

        n = s.intersection(d)
        assert n.contains('c') == True

        assert n.length() == 1
        assert n.size == 1


    def test_difference(self):
        s = CustomSet(['animals','love','the','free','land'])
        d = CustomSet(['animals','love','the','cage'])
        c = d.difference(s)

        assert c.contains('cage') == True

    def test_difference_fail(self):
        s = CustomSet(['animals','love','the','free','land'])
        d = CustomSet(['animals','love','the','free', 'land'])
        c = d.difference(s)

        assert c.contains('land') == False


    def test_difference_add(self):
        s = CustomSet()
        d = CustomSet()

        s.add('little')
        s.add('mice')
        s.add('men')

        d.add('little')
        d.add('mice')
        d.add('woman')

        c = d.difference(s)

        assert c.contains('woman') == True



    def test_is_subset(self):
        s = CustomSet()
        d = CustomSet()
        s.add('a')
        s.add('b')
        s.add('c')
        d.add('b')

        assert s.is_subset(s) is True
        assert s.is_subset(d) == True


    def test_is_subset_fail(self):
        s = CustomSet()
        d = CustomSet()
        s.add('a')
        s.add('b')
        s.add('c')

        d.add('b')
        d.add('a')
        d.add('g')
        d.add('x')

        assert s.is_subset(d) == False

    def test_is_subset_fail2(self):
        s = CustomSet()
        d = CustomSet()
        s.add('a')
        s.add('b')
        s.add('c')

        d.add('b')
        d.add('a')
        d.add('g')


        assert s.is_subset(d) == False
