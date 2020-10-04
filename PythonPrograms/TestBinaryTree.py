import unittest
from collections import namedtuple
from PythonPrograms import BinaryTree

if __name__ == "__main__":
    # import sys  sys.argv = ['', 'Test.testName']
    #unittest.main()

    final_list = []
    personer_list = namedtuple('personer', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])
    try:
        with open("personer.dta", "r", encoding='latin1') as file:
            for lines in file:
                data = lines.strip("\n").split(';')
                personer = personer_list(etternavn=data[0], fornavn=data[1], adresse=data[2],
                                         postnummer=data[3], poststed=data[4])
                final_list.append(personer)
    except FileNotFoundError as err:
        print(err)
    finally:
        file.close()
    personer_tuples = ([personer.etternavn for personer in final_list])

    node = BinaryTree.BinaryTree(personer_tuples)
    BinaryTree.BinaryTree.insert(node)


    #def test_insert(self):
    #    self.assertIn("Kristiansen", final_list)