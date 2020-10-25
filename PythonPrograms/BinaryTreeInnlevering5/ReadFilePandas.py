# Oblig 5, Halil Ibrahim Keser
from collections import namedtuple
from PythonPrograms.BinaryTreeInnlevering5.BinaryTree import BinaryTree
from PythonPrograms.BinaryTreeInnlevering5.BinaryTreeNode import BinaryTreeNode
import pandas as pd

# 1: A)
colNames = ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed']
PATH = 'Personer.dta'
person_list = []
person_tuples = namedtuple('personer', ['index', 'etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])
personer = pd.read_csv(PATH, header=None, sep='\n', delimiter=';', engine='python',
                       names=colNames, encoding='latin1',
                       dtype=namedtuple(typename='person',
                                        field_names='etternavn fornavn adresse postnummer poststed'))

for row in personer.itertuples(index=True, name='person'):
    personer = person_tuples(index=row[0], etternavn=row[1], fornavn=row[2], adresse=row[3],
                             postnummer=row[4], poststed=row[5])
    person_list.append(personer)

# 1: B)
binaryTree = BinaryTree()
for personer in person_list:
    binaryTree.insert(value=personer)

# 1: C)
