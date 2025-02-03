i = 0
total_curso = 0
titulo = """
\t*******************************
\t    Simulador de alumnos
\t*******************************
"""
mesnsaje_rechazo = "Dato no valido"
inicio = "Ingrese las notas del estudiante " 
print(titulo)
students = float(input("Ingrese la cantidad de estudiantes\n"))
students = int(students)

while students <= 0:
    print(mesnsaje_rechazo)
    students = float(input("Ingrese la cantidad de estudiantes\n"))
    students = int(students)

while i < students:
    i+=1
    print(inicio, i)
    nota_problema = (input("Ingrese la nota de problemas\n"))
    nota_problema = float(nota_problema)
    while nota_problema < 0 or nota_problema > 10:
        print(mesnsaje_rechazo)
        nota_problema = (input("Ingrese la nota de problemas\n"))
        nota_problema = float(nota_problema)
        
    nota_teorica = (input("Ingrese la nota teorica\n"))
    nota_teorica = float(nota_teorica)
    while nota_teorica < 0 or nota_teorica > 10:
        print(mesnsaje_rechazo)
        nota_teorica = (input("Ingrese la nota de problemas\n"))  
        nota_teorica = float(nota_teorica)  
    
    nota_prueba = (input("Ingrese la nota de la prueba\n"))
    nota_prueba = float(nota_prueba)
    while nota_prueba < 0 or nota_prueba > 10:
        print(mesnsaje_rechazo)
        nota_prueba = (input("Ingrese la nota de problemas\n"))
        nota_prueba = float(nota_prueba)
        
    total_student = ((nota_problema * 0.10) + (nota_teorica * 0.40) + (nota_prueba * 0.50))
    print("El estudiante tiene un promedio de ", total_student)
    total_curso += total_student
    
prom_final = float(total_curso/students)
print("El promedio del curso es ", prom_final)