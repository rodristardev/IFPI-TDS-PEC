"""02. Escreva um programa que ler o valor para um lado de um quadrado.
Calcule o mostre a área e o perímetro desse quadrado."""

#função que calcula a area.
def area(l):
    return l ** 2

#função que calcula o perimetro.
def perimetro(l):
    return l * 4

#Bloco principal
def main():
    lado = float(input("Insira o valor do lado:"))

    a = f"{area(lado):.4f}"
    p = f"{perimetro(lado):.4f}"

    print(f"{str(a)[:10]:>10}")
    print(f"{str(p)[:10]:>10}")

if __name__ == "__main__":
    main()