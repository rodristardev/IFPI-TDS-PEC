
def eh_letra_numero(l):
    return ("A" <= l <= "Z" or "a" <= l <= "z") or ("0" <= l <= "9")

def main():

    caractere = str(input()).strip()
    print(eh_letra_numero(caractere))

if __name__ == "__main__":
    main()