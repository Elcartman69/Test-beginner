import secrets
import string

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    caracteres = ''
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Pelo menos uma categoria de caractere deve ser selecionada.")

    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho_senha = int(input("Digite o tamanho desejado para a senha: "))
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    try:
        senha_gerada = gerar_senha(tamanho_senha, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)
        print(f"\nSenha gerada: {senha_gerada}")
    except ValueError as e:
        print(f"\nErro: {e}")