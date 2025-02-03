mayor = 0
menor = 11
total_grades = 0
average_pass = 0
average_fail = 0
i = 0

titulo = """\t
*******************************
    Simulador de notas
*******************************
"""
print(titulo)

estudiantes = input("Ingrese la cantidad de estudiantes\n")
estudiantes = float(estudiantes)

estudiantes = int(estudiantes)

while estudiantes <= 0:
    print("Dato no valido")
    estudiantes = input ("Ingrese la cantidad de estudiantes\n")
    estudiantes = int(estudiantes)
    
while i < estudiantes:
    i+=1
    print("Ingrese las notas del estudiantes ", i)
    nota_final = float(input("Ingrese la nota final del estudiantes\n"))
    while nota_final <=0 or nota_final > 10:
        print ("Dato no valido")
        nota_final = input ("Ingrese la nota final del estudiante\n") 
        nota_final = int (nota_final)
        
    if nota_final > mayor:
        mayor = nota_final
    if nota_final < menor:
        menor = nota_final
    if 7 <= nota_final <= 10:
        average_pass += 1
    if 0 <= nota_final < 7:
        average_fail += 1
    total_grades += nota_final

print("La cantidad de estudiantes aprobados es ", average_pass)
print("\nLa cantidad de estudiantes desaprobados es ", average_fail)
print("\nLa mayor nota es  ", mayor)
print("\nLa menor nota es  ", menor)

