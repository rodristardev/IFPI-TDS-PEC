
def eh_consoante(l):
    return l not in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U" ) and ("A" <= l <= "Z" or "a" <= l <= "z")
def main():

    letra = str(input()).strip()
    print(eh_consoante(letra))

if __name__ == "__main__":
    main()