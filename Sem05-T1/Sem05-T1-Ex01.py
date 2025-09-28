"""01. Escreva um programa que ler três valores inteiros (a, b, e c).
Calcule o mostre o resultado da função:"""

#função que calcula expressão desejada.
def funcao(a, b, c):
    func = (2 * a) + (5 * b) - c
    return func

#Bloco Principal
def main():

    numa = int(input("Insira o valor de A:"))
    numb = int(input("Insira o valor de B:"))
    numc = int(input("Insira o valor de C:"))

    print(funcao(numa, numb, numc))

if __name__=="__main__":
    main()