
def conveter(m):
    return m // 60

def minutos_extras(m):
    return m % 60

def main():

    minutos = int(input())
    print(f"{conveter(minutos)}:{minutos_extras(minutos)}")

if __name__ == "__main__":
    main()