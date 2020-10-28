# Oblig 5, Halil Ibrahim Keser

from PythonPrograms.BinaryTreeInnlevering5.BinaryTree import BinaryTree

import pandas as pd

binaryTree = BinaryTree()
list_person_namedTuples1 = []
level_list = []


def lesFilMedPandas():
    colNames = ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed']
    PATH = 'Personer.dta'
    personer1 = pd.read_csv(PATH, header=None, sep='\n', delimiter=';', engine='python',
                            names=colNames, encoding='latin1')
    return personer1


def leggNamedTuplesIList(person):
    for row in person.itertuples(index=False, name='Person'):
        list_person_namedTuples1.append(row)
    return list_person_namedTuples1


def leggInnIBinaryTree(personer_namedTuples):
    for p in personer_namedTuples:
        binaryTree.insert(value=p)


def leggInnLevelIEgenListe():
    for i in range(0, 100000):
        if i == 0 or i == 9 or i == 99 or i == 999 or i == 9999 or i == 99999:
            tuples_with_levels = list_person_namedTuples[i]
            level_list.append(tuples_with_levels)
            level_list.append(binaryTree.find(list_person_namedTuples[i]).level)
    return level_list


personer = lesFilMedPandas()
list_person_namedTuples = leggNamedTuplesIList(personer)
leggInnIBinaryTree(list_person_namedTuples)
leggInnLevelIEgenListe()

person1 = binaryTree.find(list_person_namedTuples[0])
person10 = binaryTree.find(list_person_namedTuples[9])
person100 = binaryTree.find(list_person_namedTuples[99])
person1000 = binaryTree.find(list_person_namedTuples[999])
person10000 = binaryTree.find(list_person_namedTuples[9999])
person100000 = binaryTree.find(list_person_namedTuples[99999])

print("\nFør sletting:")
print("Person 1: \t\t", person1.value, "Level: ", person1.level)
print("Person 10: \t\t", person10.value, "Level: ", person10.level)
print("Person 100: \t", person100.value, "Level: ", person100.level)
print("Person 1000: \t", person1000.value, "Level: ", person1000.level)
print("Person 10000: \t", person10000.value, "Level: ", person10000.level)
print("Person 100000: \t", person100000.value, "Level: ", person100000.level)

binaryTree.delete(person1000)
binaryTree.delete(person10000)

# person1 = binaryTree.find(list_person_namedTuples[0])
person10 = binaryTree.find(list_person_namedTuples[9])
person100 = binaryTree.find(list_person_namedTuples[99])
person1000 = binaryTree.find(list_person_namedTuples[999])
person10000 = binaryTree.find(list_person_namedTuples[9999])
person100000 = binaryTree.find(list_person_namedTuples[99999])

print("\nEtter sletting:")
# print("Person 1: \t\t", person1.value)
print("Person 10: \t\t", person10.value)
print("Person 100: \t", person100.value)
print("Person 1000: \t", person1000.value)
print("Person 10000: \t", person10000.value)
print("Person 100000: \t", person100000.value)

person8 = binaryTree.find(list_person_namedTuples[8])
person50 = binaryTree.find(list_person_namedTuples[50])
person400 = binaryTree.find(list_person_namedTuples[400])
person2300 = binaryTree.find(list_person_namedTuples[2300])
person8000 = binaryTree.find(list_person_namedTuples[8000])
person49999 = binaryTree.find(list_person_namedTuples[49999])
person75000 = binaryTree.find(list_person_namedTuples[75000])

print("\nInnleveringsdel")
print("Person 8: \t\t", person8.value)
print("Person 50: \t\t", person50.value)
print("Person 400: \t", person400.value)
print("Person 2300: \t", person2300.value)
print("Person 8000: \t", person8000.value)
print("Person 49999: \t", person49999.value)
print("Person 75000: \t", person75000.value)
