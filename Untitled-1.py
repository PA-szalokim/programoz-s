
szo = None
while szo != '':
  szo = input('Kérem a nevét: ')    
print(f'A neve {szo} 10d osztaly tanuloja')    

def adatbekeres():
 nev1 = None
while nev1 != '':
    nev1 = input('Kerek egy nevet: ')
    print(f'A neve {nev1}, 11d osztalyos tanuloja.')

adatbekeres()


def adatbekeres_break():
  while True:
    nev2= input('Kerek egy masik nevet: ')
    if nev2 == " ":
        break
    print(f' a neve {nev2}, 12.d osztalyos tanuloja.')