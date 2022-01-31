print("Introduzca su mail")
mail = str(input())
indiceDe = int(mail.index("@"))
mailnuevo = mail.replace(mail, mail[0:indiceDe + 1])
mailnuevo += "ceu.es"
print(mailnuevo)