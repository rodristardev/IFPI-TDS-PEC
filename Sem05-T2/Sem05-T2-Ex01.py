"""01. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se
for uma vogal ou o valor booleano False (falso) caso contrário."""

#função que verifica se o caractere está dentro do conjunto de vogais.
def eh_vogal(l):
    return l in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")

#Bloco principal.
def main():

    letra = str(input("Insira um caractere: ")).strip()
    print(eh_vogal(letra))

if __name__ == "__main__":
    main()