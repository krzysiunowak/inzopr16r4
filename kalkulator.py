<<<<<<< HEAD
def dodawanie():
    a = int(input("Podaj a:"))
    b = int(input("Podaj b:"))
    print (a+b)


dodawanie()
input()
=======



	
	
input()
>>>>>>> zmiana_funkcji_dodawania
def dodawanie(a,b):
    return a+b

try:	
	a = int(input("Podaj pierwszą liczbę:"))
	b = int(input("Podaj drugą liczbę:"))
	print(dodawanie(a,b))
except ValueError as ve:
	print("Wprowadzono błędne dane")
	
def get_info():
	return "To jest program kalkulator stworzony przez Twoją starą"
	
print (get_info())
print()
