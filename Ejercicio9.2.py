fecha = input("Fecha de nacimiento (dd/mm/aaaa):\n")
dia = fecha[:fecha.find("/")]
ma = fecha[fecha.find("/")+1:]
mes = ma[:ma.find("/")]
año = ma[ma.find("/")+1:]

print("Dia", dia)
print("Mes", mes)
print("Año", año)

