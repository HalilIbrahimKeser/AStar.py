# Oblig 5, Halil Ibrahim Keser

from PythonPrograms.BinaryTreeInnlevering5.BinaryTree import BinaryTree
from PythonPrograms.BinaryTreeInnlevering5.BinaryTreeNode import BinaryTreeNode

from collections import namedtuple
import pandas as pd

binaryTree = BinaryTree()


def lesFilMedPandas():
    colNames = ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed']
    PATH = 'Personer.dta'
    person = pd.read_csv(PATH, header=None, sep='\n', delimiter=';', engine='python',
                         names=colNames, encoding='latin1')
    return person


def leggInnSomNamedTuples(person):
    list_person_tuples = []
    for row in person.itertuples(index=False, name='Person'):
        list_person_tuples.append(row)
    return list_person_tuples


def leggInnIBinaryTree(namedTuple):
    for i in namedTuple:
        binaryTree.insert(value=i)


def settOppLevel():
    level_list = []
    tuples_with_levels = namedtuple('tuples_with_levels', 'etternavn, fornavn, adresse, postnummer, poststed, level')
    for i in range(0, 100000):
        if i == 0 or i == 9 or i == 99 or i == 999 or i == 9999 or i == 99999:
            tuples_with_levels = person_list_tuples[i]
            level_list.append(tuples_with_levels)
            level_list.append(binaryTree.find(person_list_tuples[i]).level)
    for i in level_list:  # Print, fjernes om man ikke ønsker print
        print(i)
    return level_list


person = lesFilMedPandas()
person_list_tuples = leggInnSomNamedTuples(person)
leggInnIBinaryTree(person_list_tuples)
settOppLevel()
# levelListe = settOppLevel()
# print(levelListe)

person1000 = binaryTree.find(person_list_tuples[999])
person10000 = binaryTree.find(person_list_tuples[9999])
binaryTree.delete(person1000)
binaryTree.delete(person10000)
