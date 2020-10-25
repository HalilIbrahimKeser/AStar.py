# Oblig 5, Halil Ibrahim Keser
from collections import namedtuple
from PythonPrograms.BinaryTreeInnlevering5.BinaryTree import BinaryTree
from PythonPrograms.BinaryTreeInnlevering5.BinaryTreeNode import BinaryTreeNode
import pandas as pd


# 1: A)
class Innlesning:
    def __init__(self):
        self.PATH = 'Personer.dta'
        self.colNames = ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed']
        self.binaryTree = BinaryTree()
        self.personer = pd.read_csv(self.PATH, header=None, sep='\n', delimiter=';', engine='python',
                                    names=self.colNames, encoding='latin1',
                                    dtype=namedtuple(typename='personer',
                                                     field_names='etternavn fornavn adresse postnummer poststed'))


# 1: B)
        for person in self.personer:
            self.binaryTree.insert(value=person)
# 1: C)
