print("Witaj w kalkulatorze!")
print()
print("Dostępne operatory:")
print("Aby dodać liczby wpisz +")
print("Aby odjąć liczby wpisz -")
print("Aby pomnożyć liczby wpisz *")
print("Aby podzielić liczby wpisz /")

operator = input("Podaj operator ")

def dodawanie(l1 , l2):
    return l1+l2
def odejmowanie(l1, l2):
    return l1-l2
def mnozenie(l1, l2):
    return l1*l2
def dzielenie(l1, l2):
    return l1/l2

operator_list = [('+', dodawanie), ('-', odejmowanie), ('*', mnozenie),('/', dzielenie)]

for op in operator_list:
    if operator == op[0]:
        break
else:
    print("Operator nie jest obsługiwany")
    exit()
try:
    liczba1 = int(input("Podaj pierwszą liczbę "))
    liczba2 = int(input("Podaj drugą liczbę "))

    for op in operator_list:
        if operator == op[0]:
            print("Wynik działania: ", op[1](liczba1, liczba2))

except ValueError:
    print("Podany parametr nie jest liczbą")