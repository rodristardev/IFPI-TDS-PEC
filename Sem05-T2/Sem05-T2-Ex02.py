"""02. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro)
se for uma letra (vogal ou consoante) ou o valor booleano False (falso) caso contrário."""

#função que verifica se um caracetere é uma letra.
def eh_letra(l):
    return "A" <= l <= "Z" or "a" <= l <= "z"

#Bloco principal
def main():

    caractere = str(input("Insira um caractere: ")).strip()
    print(eh_letra(caractere))

if __name__ == "__main__":
    main()