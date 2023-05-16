from random import choice

# numero_digitos = int(input("quantos caracteres a senha deve ter?"))
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "1234567890"
especiais ="!@"
opcoes = [letras_maiusculas, letras_minusculas, numeros, especiais]
def gerador_de_senha(numero_caracteres, caracteres):
    senha = ""
    for i in range(numero_caracteres):
        senha += choice(caracteres)
    return senha


