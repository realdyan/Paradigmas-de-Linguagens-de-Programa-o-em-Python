# -- Conversão de tipos --
def conversao_tipos():
    print("-------------------------")
    nota1_str = input("Nota1: Digite um número inteiro: ")
    nota2_str = input("Nota2: Digite um número flutuante: ")
    nota3_str = input("Nota3: Digite outro número inteiro: ")

    nota1 = int(nota1_str)
    nota2 = float(nota2_str)
    nota3 = int(nota3_str)
    media = ((nota1 + nota2 + nota3) / 3)
    media_formatada = f"{media:.2f}" # Formata a média para 2 casas decimais formatação string
    print("-------------------------")
    print("Número inteiro 1:", nota1)
    print("Número flutuante:", nota2)
    print("Número inteiro 2:", nota3)
    print("-------------------------")
    print("Média: ", media_formatada)


# -- FUNÇÃO PRINCIPAL(MAIN) --
def main():

    # -- Função Conversão de Tipos --
    print("\n=== Conversão de Tipos ===")
    conversao_tipos()
    print("=== Fim Conversão de Tipos ===\n")


if __name__ == "__main__":
    main()
