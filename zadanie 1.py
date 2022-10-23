'''
Napisz prosty kalkulator płacy netto/brutto w Polsce razem ze wszystkimi obciążeniami tj.
ubezpieczenie emerytalne, rentowe, chorobowe, zdrowotne, zaliczka na PIT.
'''

BruttoNetto = int(input("Wybierz rodzaj wynagrodzenia (1. Brutto 2. Netto): "))

if BruttoNetto == 1:

    wynagrodzenie_brutto = float(input('Podaj wysokość wynagrodzenia w brutto: '))

    def oblicz_ubez_emerytalne(brutto):
        return brutto * 0.0976
    def oblicz_ubez_rentowne(brutto):
        return brutto * 0.015
    def oblicz_ubez_chorobowe(brutto):
        return brutto * 0.0245
    def oblicz_ubez_zdrowotne_podl_odl(kwota_bez_skladek):
        return kwota_bez_skladek * 0.0775
    def oblicz_ubez_zdrowotne(kwota_bez_skladek):
        return kwota_bez_skladek * 0.09
    def oblicz_zaliczke(brutto, skladki):
        podst_opod = brutto - skladki - 250
        pod_nalezny = podst_opod * 0.17 - 43.76
        ubezp_zdrwotne = oblicz_ubez_zdrowotne_podl_odl(brutto - skladki)
        if ubezp_zdrwotne >= pod_nalezny:
            return 0
        else:
            return pod_nalezny - ubezp_zdrwotne
    skladki = oblicz_ubez_emerytalne(wynagrodzenie_brutto) + oblicz_ubez_rentowne(wynagrodzenie_brutto) + oblicz_ubez_chorobowe(wynagrodzenie_brutto)
    zaliczka = oblicz_zaliczke(wynagrodzenie_brutto,skladki)
    print(skladki)
    print('Wnagrodzenie netto',round(wynagrodzenie_brutto - skladki - oblicz_ubez_zdrowotne(wynagrodzenie_brutto-skladki) - zaliczka,2))

elif BruttoNetto ==2:

    wynagrodzenie_netto = float(input('Podaj wysokość wynagrodzenia w netto: '))

    def oblicz_ubez_emerytalne(netto):
        return netto * 9.76 / 109.76
    def oblicz_ubez_rentowne(netto):
        return netto * 1.5 / 101.5
    def oblicz_ubez_chorobowe(netto):
        return netto * 2.45 / 102.45
    def oblicz_ubez_zdrowotne_podl_odl(kwota_bez_skladek):
        return kwota_bez_skladek * 7.75 / 107.75
    def oblicz_ubez_zdrowotne(kwota_bez_skladek):
        return kwota_bez_skladek * 9 / 109
    def oblicz_zaliczke(netto, skladki):
        podst_opod = netto + skladki + 250
        pod_nalezny = podst_opod * 17  / 117 - 43.76
        ubezp_zdrwotne = oblicz_ubez_zdrowotne_podl_odl(netto + skladki)
        if ubezp_zdrwotne >= pod_nalezny:
            return 0
        else:
            return pod_nalezny - ubezp_zdrwotne


    wynagrodzenie = wynagrodzenie_netto * 17 / 117 + wynagrodzenie_netto
    skladki = oblicz_ubez_emerytalne(wynagrodzenie) + oblicz_ubez_rentowne(wynagrodzenie) + oblicz_ubez_chorobowe(wynagrodzenie)
    zaliczka = oblicz_zaliczke(wynagrodzenie, skladki)
    print(skladki)
    print('Wnagrodzenie brutto',round(wynagrodzenie_netto + skladki + oblicz_ubez_zdrowotne(wynagrodzenie + skladki) + zaliczka,2))

else:
    print('Podano złe dane.')
