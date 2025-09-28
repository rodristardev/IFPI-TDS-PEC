
def eh_letra(l):
    return "A" <= l <= "Z" or "a" <= l <= "z"

def main():

    caractere = str(input()).strip()
    print(eh_letra(caractere))

if __name__ == "__main__":
    main()