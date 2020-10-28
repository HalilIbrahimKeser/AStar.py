# Oblig 5, Halil Ibrahim Keser

from PythonPrograms.BinaryTreeInnlevering5.BinaryTree import BinaryTree

import pandas as pd

binaryTree = BinaryTree()
level_list = []
count_levels = {}


def lesFilMedPandas():
    colNames = ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed']
    PATH = 'Personer.dta'
    personer1 = pd.read_csv(PATH, header=None, sep='\n', delimiter=';', engine='python',
                            names=colNames, encoding='latin1')
    return personer1


def leggNamedTuplesIList(df):
    list_person_namedTuples1 = []
    for row in df.itertuples(index=False, name='Person'):
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


def tellOppLevels():
    for i in list_person_namedTuples:
        if binaryTree.find(i) is not None:
            level = binaryTree.find(i).level
            if level in count_levels:
                count_levels[level] += 1
            else:
                count_levels[level] = 1
    return count_levels


df = lesFilMedPandas()
list_person_namedTuples = leggNamedTuplesIList(df)
leggInnIBinaryTree(list_person_namedTuples)
leggInnLevelIEgenListe()

# Oppgave 1 C, Skriv ut nivået og verdien for rad nr 1, 10, 100, 1000, 10000, 100000 fra filen Personer.dta
print("\nOppgave 1: Noder og nivåer:")
print(binaryTree.find(list_person_namedTuples[0]).value,
      "level=", binaryTree.find(list_person_namedTuples[0]).level)
print(binaryTree.find(list_person_namedTuples[9]).value,
      "level=", binaryTree.find(list_person_namedTuples[9]).level)
print(binaryTree.find(list_person_namedTuples[99]).value,
      "level=", binaryTree.find(list_person_namedTuples[99]).level)
print(binaryTree.find(list_person_namedTuples[999]).value,
      "level=", binaryTree.find(list_person_namedTuples[999]).level)
print(binaryTree.find(list_person_namedTuples[9999]).value,
      "level=", binaryTree.find(list_person_namedTuples[9999]).level)
print(binaryTree.find(list_person_namedTuples[99999]).value,
      "level=", binaryTree.find(list_person_namedTuples[99999]).level)

# Oppgave 2 B, Slett rad nr. 1000 og 10000
print("\nOppgave 2 B: Før sletting:")
print(binaryTree.find(list_person_namedTuples[999]).value, binaryTree.find(list_person_namedTuples[999]).level)
print(binaryTree.find(list_person_namedTuples[9999]).value, binaryTree.find(list_person_namedTuples[999]).level)

binaryTree.delete(list_person_namedTuples[999])
binaryTree.delete(list_person_namedTuples[9999])

print("\nEtter sletting:")
print(binaryTree.find(list_person_namedTuples[999]))
print(binaryTree.find(list_person_namedTuples[9999]))

print("\nOppgave 3: Innleveringsdel")
print("Person 8, \t\tLevel= ", binaryTree.find(list_person_namedTuples[7]).level)
print("Person 50, \t\tLevel= ", binaryTree.find(list_person_namedTuples[49]).level)
print("Person 400, \tLevel= ", binaryTree.find(list_person_namedTuples[399]).level)
print("Person 2300, \tLevel= ", binaryTree.find(list_person_namedTuples[2299]).level)
print("Person 8000, \tLevel= ", binaryTree.find(list_person_namedTuples[7999]).level)
print("Person 49999, \tLevel= ", binaryTree.find(list_person_namedTuples[49998]).level)
print("Person 75000, \tLevel= ", binaryTree.find(list_person_namedTuples[74999]).level)

print("\nAntall noder i hvert nivå")
dict_list = tellOppLevels()
for i in dict_list:
    print("Nivå: ", i, ", Noder: ", dict_list[i])
