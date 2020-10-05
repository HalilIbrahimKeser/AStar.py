import unittest
from collections import namedtuple
from PythonPrograms import BinaryTree

if __name__ == "__main__":
    # import sys  sys.argv = ['', 'Test.testName']
    #unittest.main()

    personer = []
    Person = namedtuple('Person', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])
    try:
        with open("personer.dta", "r", encoding='latin1') as file:
            for lines in file:
                data = lines.strip("\n").split(';')
                p = Person(etternavn=data[0], fornavn=data[1], adresse=data[2],
                           postnummer=data[3], poststed=data[4])
                personer.append(p)
    except FileNotFoundError as err:
        print(err)
    finally:
        file.close()
    personer_tuples = [personer for personer in personer]

    node = BinaryTree.BinaryTree()
    for nodes in personer_tuples:
        node.insert(value=nodes)


    #def test_insert(self):
     #   self.assertIn("Kristiansen", nodes)
