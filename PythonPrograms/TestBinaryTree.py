import unittest
from collections import namedtuple
from PythonPrograms import BinaryTree

if __name__ == "__main__":
    # import sys  sys.argv = ['', 'Test.testName']
    # unittest.main()

    personer = []
    Person = namedtuple('Person', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])
    list = [


    ]

    personer_tuples = [Person for Person in personer]

    node = BinaryTree.BinaryTree()
    for nodes in personer_tuples:
        node.insert(value=nodes)

    print(node)

    # def test_insert(self):
    #   self.assertIn("Kristiansen", nodes)
