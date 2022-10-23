'''
Napisz program, który będzie prostym testem składającym się z 10 pytań z wiedzy
informatycznej. Na końcu program wystawi ocenę użytkownikowi od niedostatecznej do
celującej. Przyjmij odpowiednie kryteria.
'''

pytania = []
pytania.append(('Jak często należy robić przerwy w pracy przed komputerem: \n a. co najmniej raz na godzinę \n '
                'b. dokładnie co 3 godziny \n c. nie trzeba robić przerwy \n', 'a'))
pytania.append(('Zalecana odległośc od monitora: \n a. 20-30 cm \n b. powyżej 130cm \n c. 40-70 cm \n', 'c'))
pytania.append(('Python jest: \n a. językiem wysokopoziomowym \n b. językiem nikospoziomowym \n', 'a'))
pytania.append(('Zapis programu komputerowego przy pomocy określonego języka opragromowania to kod źródłowy: \n a. prawda \n b. fałsz \n', 'a'))
pytania.append(('Narzędzie pozwalające na kontrolę wykonywania kodu programu to kompilator: \n a. prawda \n b.fałasz \n', 'b'))
pytania.append(('Co to jest "zip": \n a. program edycji plików \n b. format kompresji plików \n','b'))
pytania.append(('Podstawowy edytor graficzny Windows to:\n a. Paint \n b. Word \n c. Gimp \n','a'))
pytania.append(
    ('.mp3 to format plików: \n a. muzycznych \n b. graficznych \n c. tekstowych \n','a'))
pytania.append(
    ('Jak potoczne nazywamy symbol "@" \n a. żaba \n b. koza \n c. małpa \n','c'))
pytania.append(
    ('Aplikacja może składać się z wielu algorytmów i instrukcji: \n a. prawda \n b. fałsz \n','a'))

punkty = 0
i = 0
while i < len(pytania):
    print(pytania[i][0])
    x = input('Podaj odpowiedź: ')
    if x == pytania[i][1]:
        punkty += 1
    i += 1
print('Liczba punktów jakie uzyskałeś/aś: ', punkty)

if punkty == 10:
    print('Otzrymałeś ocenę celującą.')
elif punkty == 9:
    print('Otzrymałeś ocenę bardzo dobrą.')
elif punkty == 8:
    print('Otzrymałeś ocenę dobrą.')
elif punkty == 7:
    print('Otzrymałeś ocenę dostaczną.')
elif punkty == 6:
    print('Otzrymałeś ocenę dopuszczającą.')
else:
    print('Otzrymałeś ocenę niedostateczną.')
