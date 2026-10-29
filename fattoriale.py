n = int(input("inserisci un numero"))
def fattoriale(num):
    fatt = 1
    for i in range(1, num + 1):
        fatt *= i
    return fatt

n = int(input("inserisci un numero intero positivo: "))
fatt = fattoriale(n)
print(f"il fattoriale di {n} è {fatt}")