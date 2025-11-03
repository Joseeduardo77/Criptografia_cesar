# main.py
from cesar import criptografar, descriptografar
import time

def menu():
    while True:
        print("\n==============================")
        print("   SISTEMA DE CRIPTOGRAFIA")
        print("       Cifra de César")
        print("==============================")
        print("1 - Criptografar mensagem")
        print("2 - Descriptografar mensagem")
        print("3 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mensagem = input("\nDigite a mensagem (máx. 128 caracteres): ")
            if len(mensagem) > 128:
                print("Erro: a mensagem não pode ter mais de 128 caracteres!")
                continue

            try:
                deslocamento = int(input("Digite o número de deslocamento (ex: 3): "))
            except ValueError:
                print("Erro: digite um número válido.")
                continue

            print("\nCriptografando...")
            time.sleep(1.2)  # efeito visual
            texto_cifrado = criptografar(mensagem, deslocamento)
            print("\nMensagem criptografada:")
            print(texto_cifrado)

        elif opcao == "2":
            mensagem_cifrada = input("\nDigite a mensagem criptografada: ")

            try:
                deslocamento = int(input("Digite o número de deslocamento usado: "))
            except ValueError:
                print("Erro: digite um número válido.")
                continue

            print("\nDescriptografando...")
            time.sleep(1.2)
            texto_decifrado = descriptografar(mensagem_cifrada, deslocamento)
            print("\nMensagem descriptografada:")
            print(texto_decifrado)

        elif opcao == "3":
            print("\nEncerrando o programa... 👋")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()