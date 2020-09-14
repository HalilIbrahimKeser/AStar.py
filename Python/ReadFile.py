from collections import namedtuple

data = {}
personer = namedtuple('personer', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])

try:
    with open("personer.dta") as file:
        for lines in file:
            data = [lines.strip().split(';')]
            personer = personer._make(data[0])
except FileNotFoundError as err:
    print(err)

print(data, '\n')
print(personer, '\n')
print(lines)

file.close()
