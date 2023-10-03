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
    passwords = []

    for i in range(25):
        listChar = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
        l = []
        for j in range(4):
            isTrue = bool(getrandbits(1))
            if not isTrue:
                l.append(listChar[j])

        #char = transformListIntoString(set(listChar) - set(l))
        char = transformListIntoString(set(listChar) - set([]))

        passwords.append(generatePassword(char))

    return passwords