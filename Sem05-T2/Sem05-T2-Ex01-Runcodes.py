
def eh_vogal(l):
    return l in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")

def main():

    letra = str(input()).strip()
    print(eh_vogal(letra))

if __name__ == "__main__":
    main()