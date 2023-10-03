import generatePassword

listPassword = generatePassword.main()

for password in listPassword:
    if len(password) >= 8 and any(p.isupper() for p in password):
        print(f"{password} -> Aprovado")
    else:    
        print(f"{password} -> Reprovado")
