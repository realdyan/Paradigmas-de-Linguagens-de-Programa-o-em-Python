def soma( a, b ):
    return a + b

def subtracao( a, b ):
    return a - b

def multiplicacao( a, b ):
    return a * b

def divisao( a, b ):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Resultados:")
    print("Soma:", soma(num1, num2))
    print("Subtração:", subtracao(num1, num2))
    print("Multiplicação:", multiplicacao(num1, num2))
    print("Divisão:", divisao(num1, num2))

if __name__ == "__main__":
    main()


