
def cesar(mensagem, chave, md):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#%&' ##Caracteres que podem ser usados
    mensagem =mensagem.upper() ##Transforma a mensagem em maiuscula
    caracter_convertido = lambda x: alfabeto[(alfabeto.find(x) + (chave*md)) % len(alfabeto)] ##Funcao que converte os caracteres em outros
    armazena = "" ##Variavel que armazena a mensagem convertida
    for i in mensagem:
        if i in alfabeto:
            armazena += caracter_convertido(i)
        else:
            armazena += i
    return armazena

