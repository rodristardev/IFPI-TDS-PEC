
def area(l):
    return l ** 2

def perimetro(l):
    return l * 4

def main():
    lado = float(input())

    a = f"{area(lado):.4f}"
    p = f"{perimetro(lado):.4f}"

    print(f"{str(a)[:10]:>10}")
    print(f"{str(p)[:10]:>10}")

if __name__ == "__main__":
    main()