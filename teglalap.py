magassag=int(input('Add meg a magassagat : '))
szelesseg= int(input(' Add meg a szelesseget :  '))
terulet= magassag*szelesseg
if magassag>szelesseg:
    print("ez egy allo teglalap, terulete:", terulet)

elif magassag<szelesseg:
    print("ez egx fekvo teglalap, terulete :", terulet)

elif magassag==szelesseg:
    print("ez egy negyzet, terulete :",terulet )




