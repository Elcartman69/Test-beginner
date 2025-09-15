import random

# Palavras-chave e possíveis respostas
respostas = {
    "saudacao": {
        "palavras": ["oi", "olá", "ei", "e aí", "salve"],
        "respostas": ["Oi!", "Olá!", "E aí?", "Salve!"]
    },
    "como_vai": {
        "palavras": ["como", "vai", "você"],
        "respostas": ["Tudo certo por aqui, e você?", "Tô bem, e você?", "De boas!"]
    },
    "despedida": {
        "palavras": ["tchau", "falou", "até", "logo"],
        "respostas": ["Até mais!", "Falou!", "Se cuida!"]
    }
}

def entender(frase):
    frase = frase.lower()
    for categoria in respostas.values():
        if any(palavra in frase for palavra in categoria["palavras"]):
            return random.choice(categoria["respostas"])
    return "Não entendi... pode explicar de outro jeito?"

def main():
    print("Chatbot simples iniciado! Digite 'sair' para encerrar.")
    while True:
        entrada = input("Você: ")
        if entrada.lower().strip() == "sair":
            print("Bot: Até a próxima!")
            break
        resposta = entender(entrada)
        print(f"Bot: {resposta}")

if __name__ == "__main__":
    main()