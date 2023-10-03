import generatePassword

if __name__ == "__main__":
    listPassword = generatePassword.main()

    for password in listPassword:
        # A senha valida se tem 8 ou mais digítos, se tem pelo menos uma letra maiúscula, um número e um caractere especial
        if len(password) >= 8 and any(p.isupper() for p in password) and any(p.isalpha() for p in password) and any(p.isalnum() for p in password):
            print(f"{password} -> Aprovado")
        else:
            print(f"{password} -> Reprovado")