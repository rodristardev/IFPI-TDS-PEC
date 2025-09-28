"""0.4 Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro)
se for uma letra (vogal ou consoante) ou um dígito (entre ‘0’ e ‘9’) ou valor booleano False (falso)
caso contrário."""

#função que verifica se um caractere é letra ou número
def eh_letra_numero(l):
    return ("A" <= l <= "Z" or "a" <= l <= "z") or ("0" <= l <= "9")

#Bloco principal
def main():

    caractere = str(input("Insira um caractere: ")).strip()
    print(eh_letra_numero(caractere))

if __name__ == "__main__":
    main()