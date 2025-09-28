
def aumento_percentual(p, v_per):
    return (p * (v_per / 100)) + p

def desconto_percentual(p, v_per):
    return p - (p * (v_per / 100))

def main():

    preco = float(input())
    percentual = float(input())

    print(f"{aumento_percentual(preco, percentual):.2f}")
    print(f"{desconto_percentual(preco, percentual):.2f}")

if __name__=="__main__":
    main()