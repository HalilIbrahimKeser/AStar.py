"""
1: Filen "Personer.dta" skal leses inn i en list persons.
Filen inneholder 100 000 rader med fiktive personalia på formatet "etternavn;fornavn;adresse;postnummer;poststed".
Dette skal gjøres i native Python, dvs. Numpy/Pandas eller andre libs skal ikke brukes.

"""
final_list = []

try:
    with open("personer.dta", "r") as file:
        for lines in file:
            data = file.readlines()
            final_list.append(data)

except FileNotFoundError as err:
    print(err)

print(final_list)

file.close()

"""
1: Legg hver rad inn i en passende datastruktur, 
feks. tuple, dict, list eller namedtuple. Skriv så ut de 5 siste radene i en celle.
"""
from collections import namedtuple

final_list = []
personer_list = namedtuple('personer', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])

try:
    with open("personer.dta") as file:
        for lines in file:
            data = lines.strip().split(';')
            personer = personer_list(etternavn=data[0], fornavn=data[1], adresse=data[2],
                                    postnummer=data[3], poststed=data[4])
            final_list.append(personer)
except FileNotFoundError as err:
    print(err)

print(final_list[-5:])

file.close()

"""
2: Hvor mange unike postnummer finnes i "Personer.dta"?"""

"""
3: Hva er de 10 vanligste etternavnene (som forekommer flest ganger) i "Personer.dta"?"""

"""
4: Implementer sorteringsalgoritmen Heap Sort og sorter listen "persons" utfra rekkefølgen radene er lest inn i. 
Ferdig implementerte funksjoner som sorted_list skal ikke benyttes. 
Skriv så ut indexene [0,20000,40000,60000,80000] fra den sorterte listen."""