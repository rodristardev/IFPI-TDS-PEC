"""03. Escreva um programa que leia um preço e um valor percentual.
Informe o preço com o aumento percentual e o preço com o desconto
percentual. Por exemplo, se for lido um preço de 100.00 e o valor
percentual de 5 o programa deve mostrar que o preço com aumento é
105.00 e o preço com desconto é 95.00."""

#funçaõ que calcula o aumento percentual
def aumento_percentual(p, v_per):
    return (p * (v_per / 100)) + p

#função que calcula o desconto percentual
def desconto_percentual(p, v_per):
    return p - (p * (v_per / 100))

#Bloco principal
def main():

    preco = float(input("Preço: "))
    percentual = float(input("Valor Percentual: "))

    print(f"{aumento_percentual(preco, percentual):.2f}")
    print(f"{desconto_percentual(preco, percentual):.2f}")

if __name__=="__main__":
    main()