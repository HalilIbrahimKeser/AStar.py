from collections import namedtuple

"""Lager tuples med personer fra filen"""
final_list = []
personer_list = namedtuple('personer', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])

try:
    with open("personer.dta", "r") as file:
        for lines in file:
            data = lines.strip().split(';')
            personer = personer_list(etternavn=data[0], fornavn=data[1], adresse=data[2],
                                     postnummer=data[3], poststed=data[4])
            final_list.append(personer)
except FileNotFoundError as err:
    print(err)
finally:
    file.close()

"""fem siste"""
print('\n', final_list[-5], '\n', final_list[-4], '\n', final_list[-3], '\n', final_list[-2], '\n', final_list[-1],
      '\n')

"""Telle antall forekomster av postnummer"""
postnummer_list = set([x.postnummer for x in final_list])

print(len(postnummer_list))

iterable_liste = set(final_list.pop(personer.postnummer))
print(iterable_liste)
