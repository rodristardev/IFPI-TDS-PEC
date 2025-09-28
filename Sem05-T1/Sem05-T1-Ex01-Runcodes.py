
def funcao(a, b, c):
    func = (2 * a) + (5 * b) - c
    return func

def main():

    numa = int(input())
    numb = int(input())
    numc = int(input())

    print(funcao(numa, numb, numc))

if __name__=="__main__":
    main()