cantidad = int(input("Cuantas ciudades deseas ingresar:"))
ciudades = set ()
for i in range(cantidad):
    pregunta = input(f"Ingrese las ciudades que guste {i + 1} :")
    ciudades.add(pregunta)

print("Las ciudades son:")
for ciudad in ciudades:
    print(ciudad)