tel = input("ingrese su numero telefonico: ")

tel2 = tel.replace("-", "").replace("+", "")
print(tel2)
print("El numero local es: " + tel2[2:11])

