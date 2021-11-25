a = ['violet', 'red', 'yellow', 'violet']
contador = 0
for i in range(0, len(a)):
    if a[i] != "violet":
        a[i] = "violet"
        contador=contador+1
print(a)
print("Se reemplazaron ", contador, "colores." )
if contador>=3:
 print("Qué arreglo de malo, llave.")

