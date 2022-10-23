'''
Dziś jest data D, M, R. Jaka data była wczoraj? Jaka data będzie jutro?(Pamiętaj o latach
przestępnych) (Dodatkowo zaimplementuj rozwiązanie pozwalające określić kiedy wypada
Wielkanoc oraz w który dzień tygodnia się urodziłeś).
'''

def JakaBylaData ():
    from datetime import date
    from datetime import timedelta

    today = date.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    print('Wczorajsza data: ',yesterday)
    print('Jutrzejsza data: ',tomorrow)
    return
JakaBylaData()

def DzienTygUro (day,mounth,year):
    from datetime import date
    narodziny = date(year,mounth,day)
    dzientyg = narodziny.strftime('%A')
    print('Dzień tygodnia twoich narodzin:',dzientyg)
    return
DzienTygUro(10,5,2001)

def DataWielkanoc():
    rok = int(input('Podaj rok: '))
    rok19 = rok % 19
    rok4 = rok % 4
    rok7 = rok % 7
    k = 24
    i = 5
    rd = (19 * rok19 + k ) % 30
    e = (2 * rok4 + 4 * rok7 + 6 * rd + i) % 7
    marca = (22 + rd + e)
    kwietnia = (rd + e - 9)
    if marca <= 31:
        print("Święta Wielkanocne wypadną: ",int(marca),'marca.')
    else:
        print("Święta Wielkanocne wypadną ",int(kwietnia), 'kwietnia.')
    return
DataWielkanoc()