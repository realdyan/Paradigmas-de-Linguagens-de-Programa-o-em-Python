# for em python usando range
def for_range():
    for i in range(10):
        print(i)

# for em python Percorrendo lista
def for_lista():
    frutas = ["maçã", "banana", "laranja", "uva"]
    for fruta in frutas:
        print(fruta)

# for em python percorrendo string
def for_string():
    palavra = "Python"
    for letra in palavra:
        print(letra)

# for em python usando range com passo
def for_range_passo():
    for i in range(0, 20, 2):
        print(i)

# for em python usando enumerate
def for_enumerate():
    frutas = ["maçã", "banana", "laranja", "uva"]
    for indice, fruta in enumerate(frutas):
        print(f"Índice: {indice}, Fruta: {fruta}")


def main():
    while True:
        opcao = input(
            "Escolha Uma opção:\n"
            "1. For com Range\n"
            "2. For com Lista\n"
            "3. For com String\n"
            "4. For com Range e Passo\n"
            "5. For com Enumerate\n"
            "0. Sair\n"
            "Digite a opção: "
        )

        if opcao == "1":
            print("\n=== For com Range ===")
            for_range()
            print("=== Fim For com Range ===\n")

        elif opcao == "2":
            print("\n=== For com Lista ===")
            for_lista()
            print("=== Fim For com Lista ===\n")

        elif opcao == "3":
            print("\n=== For com String ===")
            for_string()
            print("=== Fim For com String ===\n")

        elif opcao == "4":
            print("\n=== For com Range e Passo ===")
            for_range_passo()
            print("=== Fim For com Range e Passo ===\n")

        elif opcao == "5":
            print("\n=== For com Enumerate ===")
            for_enumerate()
            print("=== Fim For com Enumerate ===\n")

        elif opcao == "0":
            print("Saindo...\n")
            break

        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
