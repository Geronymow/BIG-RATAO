from util import console, switch_case

def main():
    console()
    desc = int(input("Escolha uma opção: "))

    while desc != 0:
        switch_case(desc)
        console()
        desc = int(input("Escolha uma opção: "))

    print("Saindo do programa...")

if __name__ == "__main__":
    main()
