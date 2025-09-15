def caixa_eletronico():
    valor = int(input("Digite o valor para saque: "))
    notas = [100, 50, 20, 10, 5, 2]
    resultado = {}

    for nota in notas:
        qtd, valor = divmod(valor, nota)
        if qtd > 0:
            resultado[nota] = qtd

    print("Notas entregues:")
    for nota, qtd in resultado.items():
        print(f"{qtd} x R${nota}")

caixa_eletronico()
