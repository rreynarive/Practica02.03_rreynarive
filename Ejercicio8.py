precio = input("Escriba el precio del producto:\n")

print("Numero de euros: ", precio[:precio.find(".")], "€")
print("Numero de monedas: ", precio[precio.find(".")+1:], "cent")