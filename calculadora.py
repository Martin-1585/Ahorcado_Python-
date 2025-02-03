titulo = "\tCalculadora básica"
menu = """-----------Menu-------------
1. Suma
2. Resta
3. Multiplicación
4. Division

Para salir escribe "SALIR"
"""
resultado = ""

print(titulo)
print(menu)

while True:
    if not resultado:
        resultado = input("Ingrese un numero\n")
        if resultado.upper() == "SALIR":
            break
        resultado = int(resultado)
    op = input("Ingrese una operacion\n")
    if op.upper() == "SALIR":
        break
    segundo_numero = input("Ingrese el segundo numero\n")
    if segundo_numero.upper == "SALIR":
        break
    segundo_numero = int(segundo_numero)
    if op.upper() == "SUMA":
        resultado += segundo_numero
        print("Suma es ", resultado)
    elif op.upper() == "RESTA":
        resultado -= segundo_numero
        print("Resta es ", resultado)
    elif op.upper() == "MULTIPLICACION":
        resultado *= segundo_numero
        print("Multiplicacion es ", resultado)
    elif op.upper() == "DIVISION":
        resultado /= segundo_numero
        print("DIvision es ", resultado)
    else:
        print("Operacion no valida")
        