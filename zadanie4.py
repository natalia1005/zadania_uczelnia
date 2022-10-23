'''
Napisz program pozwalający przeliczyć z podanych walut w dwie strony:
Baht Tajski (THB) -Dolary amerykańskie (USD).
Bitcoin (BTC) -Dolary amerykański(USD)
Ngultrum bhutański(BTN) -Dolary amerykańskie(USD)
Ugija mauretańska(MRO) -Dolary amerykańskie (USD)
Ethereum(ETH) –Dolary amerykańskie (USD)
Czy znasz jeszcze inne dziwne waluty? Zaproponuj je w swoim programie.
'''

wartosc = int(input('Podaj wartość do przeliczenia: '))

kursy = []
kursy.append(('THB', 'USD', 0.03))
kursy.append(('USD', 'THB', 29.86))

kursy.append(('BTC', 'USD', 32600.1))
kursy.append(('USD', 'BTC', 0.000031))

kursy.append(('BTN', 'USD', 0.014))
kursy.append(('USD', 'BTN', 72.81))

kursy.append(('MRO', 'USD', 0.02773))
kursy.append(('USD', 'MRO', 36.06530))

kursy.append(('ETH', 'USD', 1289.14))
kursy.append(('USD', 'ETH', 0.00078))

kursy.append(('AFG', 'USD', 0.013))
kursy.append(('USD', 'AFG', 77.18))

kursy.append(('ANG', 'USD', 0.56))
kursy.append(('USD', 'ANG', 1.79))

kursy.append(('BAM', 'USD', 0.62))
kursy.append(('USD', 'BAM', 1.61))

def przelicz(wartosc, kurs):
    print(wartosc * kurs)
    return

kurs = [item for item in kursy if item[0] == 'USD' and item[1] == 'THB']

przelicz(wartosc, kurs[0][2])