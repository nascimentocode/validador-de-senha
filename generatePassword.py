# Gera uma resposta aleatoria se vai ter ou nao um caractere minusculo, maiusculo ...

from random import choice, randint, getrandbits
import string

def transformListIntoString(list):
    char = ''
    for c in list:
        char += c
    
    return char

def generatePassword(char):
    password = ''
    passwordLength = randint(6, 20)
    for j in range(passwordLength):
        password += choice(char)

    return password

def main():
    listChar = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    passwords = []

    print("==================== GERADOR DE SENHA ====================\n")

    # questions = ["Você quer que sua senha contenha caracteres minusculos? S/N\n", 
    #                 "Você quer que sua senha contenha caracteres maiusculos? S/N\n", 
    #                 "Você quer que sua senha contenha números? S/N\n",
    #                 "Você quer que sua senha contenha caracter especial? S/N\n"]
    
    # for index, question in enumerate(questions):
    #     result = input(question)

    #     if result.upper() == 'N':
    #         listChar.pop(index)

    # S S S S
    # N N N N

    # N S S S
    # S N S S
    # S S N S
    # S S S N

    # S N N N
    # N S N N
    # N N S N
    # N N N S

    # N N S S
    # S S N N
    # N S N S
    # S N S N

    for i in range(25):
        for j in range(4):
            isTrue = bool(getrandbits(1))
            if not isTrue:
                print(f"Tentei eliminar o {j}")
                listChar.pop(j)
                j -= 1

        char = transformListIntoString(listChar)
        passwords.insert(generatePassword(char))

    print(f"Suas senhas estão prontas para testes: {passwords}")