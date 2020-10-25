# Oblig 5, Halil Ibrahim Keser
from collections import namedtuple
from PythonPrograms.BinaryTreeInnlevering5.BinaryTree import BinaryTree
from PythonPrograms.BinaryTreeInnlevering5.BinaryTreeNode import BinaryTreeNode
import pandas as pd


# 1: A)

def setOpp(self):
    self.colNames = ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed']
    self.PATH = 'Personer.dta'
    self.person_list = []
    self.person_tuples = namedtuple('person',
                                    ['index', 'etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])
    self.person = pd.read_csv(self.PATH, header=None, sep='\n', delimiter=';', engine='python',
                              names=self.colNames, encoding='latin1',
                              dtype=namedtuple(typename='person',
                                               field_names='etternavn fornavn adresse postnummer poststed'))

    for row in self.person.itertuples(index=True, name='person'):
        i = self.person_tuples(index=row[0], etternavn=row[1], fornavn=row[2], adresse=row[3],
                               postnummer=row[4], poststed=row[5])
        self.person_list.append(i)

        # 1: B)
    self.binaryTree = BinaryTree()
    for person in self.person_list:
        self.binaryTree.insert(value=person)

    # 1: C)
    row1 = self.person('0', 'KRISTIANSEN', 'MORTEN KRISTIAN', 'LEINAHYTTA 36', '7224', 'MELHUS')
    row10 = self.person('10', 'ELI', 'RITA HELEN', 'MEHEIAVEGEN 80', '4436', 'GYLAND')
    row100 = self.person('100', 'KRISTIANSEN', 'MORTEN KRISTIAN', 'LEINAHYTTA 36', '7224', 'MELHUS')
    row1000 = self.person('1000', 'ELI', 'RITA HELEN', 'MEHEIAVEGEN 80', '4436', 'GYLAND')
    row10000 = self.person('10000', 'KRISTIANSEN', 'MORTEN KRISTIAN', 'LEINAHYTTA 36', '7224', 'MELHUS')
    row100000 = self.person('100000', 'ELI', 'RITA HELEN', 'MEHEIAVEGEN 80', '4436', 'GYLAND')
    print(self.binaryTree.find(index='0'))
    print(self.binaryTree.find(row10))


if __name__ == '__main__':
    setOpp(self)
