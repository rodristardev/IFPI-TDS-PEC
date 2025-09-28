"""05. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro)
se for um SÍMBOLO (o que não é letra ou número) ou o valor booleano False (falso) caso
contrário."""

#função que verifica se um caractere é um simbolo.
def eh_simbolo(l):
    return not (("0" <= l <= "9") or ("A" <= l <= "Z") or ("a" <= l <= "z"))

#Bloco principal
def main():

    caractere = str(input("Insira um caractere: ")).strip()
    print(eh_simbolo(caractere))

if __name__ == "__main__":
    main()