"""05. Leia um número inteiro entre 1000 e 9999 e mostre o número na ordem inversa. Por exemplo,
se o número lido for 5678 deverá ser mostrado 8765."""

#função que inverte a ordem dos digitos.
def inverte(n):
    string = str(n)
    return string[::-1]

#Bloco Principal
def main():

    num = int(input("Insira um número de 1000 a 9999: "))
    print(inverte(num))

if __name__ == "__main__":
    main()