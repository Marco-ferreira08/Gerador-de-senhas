import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")
    while True:
        try:
            tamanho = int(input("Digite o tamanho desejado para a senha (mínimo 6): "))
            if tamanho < 6:
                print("O tamanho mínimo da senha é 6. Tente novamente.")
                continue

            senha_gerada = gerar_senha(tamanho)
            print(f"Sua senha gerada é: {senha_gerada}")

            nova = input("Deseja gerar outra senha? (s/n): ").strip().lower()
            if nova != 's':
                print("Obrigado por usar o Gerador de Senhas! Até a próxima.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()