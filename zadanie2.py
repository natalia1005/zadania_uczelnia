'''
Napisz program, którego zadaniem będzie konwersja wpisanych przez użytkownika wielkości
dysków twardych na ich realną pojemność. Dlaczego producenci nas oszukują?
'''

WyborWielkosci = int(input('Wybierz wielkość dysku twardego: \n 1. TB \n 2. GB \n '))
WielkoscDT = int(input('Podaj wielkość dysku twradego: '))

def RealnaWielkoscTB():
    Wielkosc = WielkoscDT * 1000 * 1000 * 1000 * 1000
    Realna = Wielkosc / 1024 /1024 /1024
    print('Pojemność realna dysku wynosi :', Realna, 'GB.')
    return

def RealnaWielkoscGB():
    wielkosc = WielkoscDT * 1000 * 1000 * 1000
    realna = wielkosc / 1024 / 1024 / 1024
    print('Pojemność realna dysku wynosi :', realna, 'GB.')
    return

if WyborWielkosci == 1:
    RealnaWielkoscTB()
else:
    RealnaWielkoscGB()