
def eh_simbolo(l):
    return not (("0" <= l <= "9") or ("A" <= l <= "Z") or ("a" <= l <= "z"))

def main():

    caractere = str(input()).strip()
    print(eh_simbolo(caractere))

if __name__ == "__main__":
    main()