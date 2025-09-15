import random

def jogo_adivinhacao():
    while True:
        numero = random.randint(1, 10)
        tentativas = 0
        limite = 3

        print("\n=== JOGO DA ADIVINHAÇÃO ===")
        print("Pense em um número de 1 a 10.")
        print(f"Você tem {limite} tentativas.\n")

        while tentativas < limite:
            try:
                chute = int(input(f"Tentativa {tentativas + 1}: "))
            except ValueError:
                print("Digite um número válido!")
                continue

            tentativas += 1

            if chute < numero:
                print("Muito baixo!")
            elif chute > numero:
                print("Muito alto!")
            else:
                print(f"Parabéns!!! Acertou em {tentativas} tentativas! O número era {numero}.")
                break
        else:
            print(f"\nQue pena. Suas tentativas acabaram! O número era {numero}.")

        jogar_novamente = input("\nQuer jogar de novo? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Valeu por jogar! Até a próxima.")
            break

jogo_adivinhacao()
