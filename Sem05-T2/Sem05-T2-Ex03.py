"""03. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro)
se for uma consoante ou o valor booleano False (falso) caso contrário."""

#função que verifica se um caractere é uma consoante
def eh_consoante(l):
    return l not in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U" ) and ("A" <= l <= "Z" or "a" <= l <= "z")

#Bloco principal
def main():

    letra = str(input("Insira o caractere:")).strip()
    print(eh_consoante(letra))

if __name__ == "__main__":
    main()