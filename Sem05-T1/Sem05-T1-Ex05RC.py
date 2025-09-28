
def inverte(n):
    string = str(n)
    return string[::-1]

def main():

    num = int(input())
    print(inverte(num))

if __name__ == "__main__":
    main()