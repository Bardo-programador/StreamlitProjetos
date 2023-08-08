class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alfabeto = alphabet
    
    def encode(self, text):
        return "".join(self.alfabeto[(self.alfabeto.find(self.key[indice%len(self.key)])+self.alfabeto.find(val))%len(self.alfabeto)] if val in self.alfabeto else val for indice, val in enumerate(text))
    
    def decode(self, text):
        return "".join(self.alfabeto[(self.alfabeto.find(val)-self.alfabeto.find(self.key[indice%len(self.key)]))%len(self.alfabeto)] if val in self.alfabeto else val for indice, val in enumerate(text))