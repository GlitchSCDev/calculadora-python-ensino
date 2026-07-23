import math

def menu():
    print("=" * 35)
    print("      CALCULADORA PYTHON")
    print("=" * 35)
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("7 - Porcentagem")
    print("8 - Resto da Divisão")
    print("9 - Divisão Inteira")
    print("0 - Sair")
    print("=" * 35)

while True:
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Calculadora encerrada.")
        break

    try:
        if opcao == "6":
            num = float(input("Digite um número: "))

            if num < 0:
                print("Não existe raiz quadrada real de número negativo.")
            else:
                print(f"Resultado: {math.sqrt(num)}")

        elif opcao == "7":
            valor = float(input("Digite o valor: "))
            porcentagem = float(input("Digite a porcentagem (%): "))

            resultado = valor * porcentagem / 100
            print(f"{porcentagem}% de {valor} = {resultado}")

        else:
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))

            if opcao == "1":
                print(f"Resultado: {num1 + num2}")

            elif opcao == "2":
                print(f"Resultado: {num1 - num2}")

            elif opcao == "3":
                print(f"Resultado: {num1 * num2}")

            elif opcao == "4":
                if num2 == 0:
                    print("Erro: divisão por zero.")
                else:
                    print(f"Resultado: {num1 / num2}")

            elif opcao == "5":
                print(f"Resultado: {num1 ** num2}")

            elif opcao == "8":
                if num2 == 0:
                    print("Erro: divisão por zero.")
                else:
                    print(f"Resultado: {num1 % num2}")

            elif opcao == "9":
                if num2 == 0:
                    print("Erro: divisão por zero.")
                else:
                    print(f"Resultado: {num1 // num2}")

            else:
                print("Opção inválida.")

    except ValueError:
        print("Digite apenas números.")

    input("\nPressione ENTER para continuar...")
    print("\n" * 2)