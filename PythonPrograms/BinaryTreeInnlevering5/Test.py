# Oblig 5, Halil Ibrahim Keser

from PythonPrograms.BinaryTreeInnlevering5.BinaryTree import BinaryTree
from PythonPrograms.BinaryTreeInnlevering5.BinaryTreeNode import BinaryTreeNode

from collections import namedtuple
import pandas as pd

btree = BinaryTree()


# def lesFilMedPandas():
#     colNames = ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed']
#     PATH = 'Personer.dta'
#     person = pd.read_csv(PATH, header=None, sep='\n', delimiter=';', engine='python',
#                          names=colNames, encoding='latin1')
#     return person

# def leggInnSomNamedTuples(person):
#     personListTuples = []
#     person_tuples = namedtuple('person', ['index', 'etternavn', 'fornavn',
#                                           'adresse', 'postnummer', 'poststed'])
#     for row in person.itertuples(index=True, name='person'):
#         personTuples = person_tuples(index=row[0], etternavn=row[1], fornavn=row[2], adresse=row[3],
#                                      postnummer=row[4], poststed=row[5])
#         personListTuples.append(personTuples)
#     return personListTuples


def import_file_into_Pandas():
    data = pd.read_table(r"Personer.dta", encoding='ANSI', delimiter=";", header=None)
    df = pd.DataFrame(data)
    df.columns = ['Lastname', 'Firstname', 'Adr', 'Postnum', 'City']
    return df


def store_as_namedTuple(df):
    list_namedtuple = []
    for row in df.itertuples(index=False, name='Person'):
        list_namedtuple.append(row)
    return list_namedtuple


def build_binaryTree(namedtuple):
    for i in namedtuple:
        btree.insert(value=i)


def save_some_in_separate_file_with_level():
    savedrows = namedtuple('savedrows', 'lastname, firstname, adress, postnumber, city, level')
    list = []
    for i in range(0, 100000):
        if i == 1 - 1 or i == 10 - 1 or i == 100 - 1 or i == 1000 - 1 or i == 10000 - 1 or i == 100000 - 1:
            savedrows = namedTuple[i]
            list.append(savedrows)
            list.append(btree.find(namedTuple[i]).level)
    return list


df = import_file_into_Pandas()
namedTuple = store_as_namedTuple(df)
build_binaryTree(namedTuple)
print(save_some_in_separate_file_with_level())
# print(namedTuple[0])
person = namedTuple[9]
print(person)
print(btree.find(person).level)
