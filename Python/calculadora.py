def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair")
        opcao = input("Digite: ")

        if opcao == "5":
            break

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if opcao == "1":
            print("Resultado:", a + b)
        elif opcao == "2":
            print("Resultado:", a - b)
        elif opcao == "3":
            print("Resultado:", a * b)
        elif opcao == "4":
            print("Resultado:", a / b if b != 0 else "Erro: divisão por zero!")
        else:
            print("Opção inválida!")

calculadora()