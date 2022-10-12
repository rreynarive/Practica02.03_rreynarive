producto = input("Introduce el producto: ")
unidades = int(input("Introduce la cantidad: "))
precio = float(input("Introduce el precio: "))
print("{producto}: {precio:6.2f}€ x {unidades:3d}= {total:8.2f}€"
      .format(producto = producto,
              precio = precio,
              unidades = unidades,
              total = unidades * precio ))