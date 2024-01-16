def dodawanie(a, b):
  return a + b

def odejmowanie(a, b):
  return a - b

def mnozenie(a, b):
  return a * b

def dzielenie(a, b):
  if b == 0:
      print("Nie można dzielić przez zero") 
  return a / b

print("Wybierz opcję: 1.Dodawanie 2.Odejmowanie 3.Mnożenie 4.Dzielenie")

wybor = input("Wybierz działanie: ")
liczba1 = float(input("Podaj pierwszą liczbę: ")) 
liczba2 = float(input("Podaj drugą liczbę: ")) 

if wybor == '1':
  print(f"{liczba1} + {liczba2} = {dodawanie(liczba1, liczba2)}")
elif wybor == '2':
  print(f"{liczba1} - {liczba2} = {odejmowanie(liczba1, liczba2)}")
elif wybor == '3':
  print(f"{liczba1} * {liczba2} = {mnozenie(liczba1, liczba2)}")
elif wybor == '4':
      print(f"{liczba1} / {liczba2} = {dzielenie(liczba1, liczba2)}")
else:
  print("Nieprawidłowy wybór")

