print('**** Velkommen til Fancy BAR ****')
name = input('heisann, hva heter du egentlig, søtnos?\n')
print('Hei ' + name + ', takk for infoen')
age = int(input('Hvor gammer er du, sweetie?\n'))

if name == 'Halil':
    print('Du er velkommen i min fancy bar')
else:
    print('Kom i morgen')

if age < 12 or age > 100:
    print('Du er for ung eller gammel')

drinks = 1
while drinks != 0:
    drinks = int(input('Mange drinker? Trykk 0 for å avbryte\n'))

i = 0
for i in range(3):
    print('Haywaan')
