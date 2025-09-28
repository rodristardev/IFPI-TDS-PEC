"""04. Escreva um programa que leia uma determinada quantidade de minutos e informe essa quantidade
convertidade para horas e minutos. Por exemplo, 220 minutos é equivalente 3 horas e 40 minutos."""

#função que converte minutos para horas.
def conveter(m):
    return m // 60

#função que separa os minutos extras.
def minutos_extras(m):
    return m % 60

#Bloco principal
def main():

    minutos = int(input("Minutos: "))
    print(f"{conveter(minutos)}:{minutos_extras(minutos)}")

if __name__ == "__main__":
    main()