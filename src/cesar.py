# cesar.py

def criptografar(mensagem, deslocamento):
    """Criptografa a mensagem usando a Cifra de César."""
    resultado = ""
    for caractere in mensagem:
        if caractere.isalpha():  # só criptografa letras
            base = ord('A') if caractere.isupper() else ord('a')
            resultado += chr((ord(caractere) - base + deslocamento) % 26 + base)
        else:
            resultado += caractere  # mantém espaços e pontuação
    return resultado


def descriptografar(mensagem_cifrada, deslocamento):
    """Descriptografa a mensagem cifrada usando a Cifra de César."""
    return criptografar(mensagem_cifrada,-deslocamento)