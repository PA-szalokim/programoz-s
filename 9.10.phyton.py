# elso feladat 9dk
idei_ev = 2022
print(type(idei_ev))
print('az idei_ev: ', idei_ev, sep='--->')
felhasznalo_kora=input('hany eves vagy?')
print( 'felhaznalo_kora valtozo ',type(felhasznalo_kora))
print('te most', felhasznalo_kora, 'eves vagy.')
felhasznalo_kora = int(felhasznalo_kora)
szuletesi_ev = idei_ev - felhasznalo_kora
print('ekkor szulettel: ',szuletesi_ev,'.', sep='')