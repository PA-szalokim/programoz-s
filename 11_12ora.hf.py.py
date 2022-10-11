egyikszam=int(input( 'kerem az elso szamot 1-100-ig :'))
masikszam=int(input('kerem a masik szamot 1-100-ig :'))
if egyikszam==masikszam:
    print('megegyezik')
elif egyikszam>masikszam:
    print('az elso szam nagyobb', egyikszam-masikszam )
elif egyikszam<masikszam:
    print('a masodik szam nagyobb', masikszam-egyikszam )
    
    
