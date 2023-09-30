from random import choice, randint, getrandbits
import string

def generatePassword(char):
    passwords = []
    for i in range(25):
        password = ''
        passwordLength = randint(6, 20)
        for j in range(passwordLength):
            password += choice(char)

        passwords.append(password)

    return passwords

def transformListIntoString(list):
    char = ''
    for c in list:
        char += c
    
    return char


def main():
    listChar = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

    print("==================== GERADOR DE SENHA ====================\n")

    # questions = ["Você quer que sua senha contenha caracteres minusculos? S/N\n", 
    #                 "Você quer que sua senha contenha caracteres maiusculos? S/N\n", 
    #                 "Você quer que sua senha contenha números? S/N\n",
    #                 "Você quer que sua senha contenha caracter especial? S/N\n"]
    
    # for index, question in enumerate(questions):
    #     result = input(question)

    #     if result.upper() == 'N':
    #         listChar.pop(index)

    for i in range(25):
        for i in range(4):
            isTrue = bool(getrandbits(1))
            if not isTrue:
                print(f"Tentei eliminar o {i}")
                listChar.pop(i)

    char = transformListIntoString(listChar)

    print(f"Sua senha criada é: {generatePassword(char)}")