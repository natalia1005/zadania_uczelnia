'''
Woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach Fahrenheita.
Napisz program który po podaniu temperatury w stopniach Celsjusza określi temperaturę w
stopniach Fahrenheita i w przypadku zamarzania bądź wrzenia program wypisze informacje
„woda zamarza”, „woda wrze”. Pamiętaj o wyświetlaniu znaku plus/minus przy temperaturze.
Dołącz funkcje odpowiadające za przeliczenie temperatury Kelwina na Fahrenhaita,
Fahrenheita na Kelwina, Kelwina na Celsjusze i Celsjusze na Kelwina. Czy znasz jeszcze jakieś
inne jednostki temperatury? Zaproponuj je w swoim programie.
'''

# przeliczanie z celcjuszy na fahrenheita
def StopnieCelFah():
    cel = float(input('Poadaj temperature w stopniach Celcjusza: '))
    print("Stopnie Celcjusza: ",cel)
    fahren = round((cel * 1.8) + 32, 2)
    print("Stopnie Fahrenhaita: ",fahren)
    return fahren

# przeliczanie z fahrenheita na celcjusze
def StopnieFahCel():
    fahren = float(input('Poadaj temperature w stopniach Fahrenheita: '))
    cel = round((fahren - 32) / 1.8, 2)
    print(round(cel,2))
    return cel

# stopnie kalwina na Fahrenheita
def StonieKalFah():
    kal = float(input('Poadaj temperature w stopniach Kalwina: '))
    fahren = round(kal * 1.8 - 459.67, 2)
    print(round(fahren,2))

    return fahren

# stopnie fahrenheita na kalwina
def StopnieFahKal():
    fahren = float(input('Poadaj temperature w stopniach Fahrenheita: '))
    kal = round(fahren + 459.67 * 1.8)
    print(round(kal,2))
    return kal

# stopnie kalwina na celcjusze
def StopnieKalCel():
    kal = float(input('Poadaj temperature w stopniach Kalwina: '))
    cel = kal - 273.15
    print(round(cel, 2))
    return cel

# stopnie celcjusza na kalwina
def StopnieCelKal():
    cel = float(input('Poadaj temperature w stopniach Celcjusza: '))
    kal = round(cel + 273.15, 2)
    print(round(kal,2))
    return kal

# stopnie celcjusza na rankine
def StopnieCelRan():
    cel = float(input('Poadaj temperature w stopniach Celcjusza: '))
    ran = round(cel * 1.8 + 491.67, 2)
    print(round(ran,2))
    return ran

# stopnie rankine na celcjusze
def StopnieRanCel():
    ran = float(input('Poadaj temperature w stopniach Rankina: '))
    cel = round(ran - 491.67 / 1.8, 2)
    print(round(cel,2))
    return cel


fahren = StopnieCelFah()

if fahren > 32.0 and fahren < 212.0:
    print('nic się nie dzieje')
elif fahren >= 212.0:
    print('Woda wrze')
else:
    print('Woda zamarza')

