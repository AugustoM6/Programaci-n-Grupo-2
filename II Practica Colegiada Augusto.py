#Ejercicio 1  César Martínez Mondragón
"""
N = int(input("Ingrese la cantidad de niños \n"))
c0_50 = 0
c51_60 = 0
c61_70 = 0
c71_100 = 0
suma = 0
for i in range(N):
    calif = int(input("Ingrese la calificación del niño \n"))
    suma += calif
    if calif >= 0 and calif <= 50:
        c0_50 += 1
    elif calif >= 51 and calif <= 60:
        c51_60 += 1
    elif calif >= 61 and calif <= 70:
        c61_70 += 1
    elif calif >= 71 and calif <= 100:
        c71_100 += 1
print("La cantidad de estudiantes que tienen calificaciones entre 0 y 50 son:", c0_50)
print("La cantidad de estudiantes que tienen calificaciones entre 51 y 60 son:", c51_60)
print("La cantidad de estudiantes que tienen calificaciones entre 61 y 70 son:", c61_70)
print("La cantidad de estudiantes que tienen calificaciones entre 71 y 100 son:", c71_100)
promedio = suma / N
print("Promedio de calificaciones:", promedio)
"""
#Ejercicio 2
total_salarios = 0
for i in range(15):
    salario = int(input("Ingrese el salario del empleado \n"))
    total_salarios += salario
dinero_adicional = 0
if total_salarios < 500 * 15:
    dinero_adicional = 500 * 15 - total_salarios
print(f"Se necesita un total de ${dinero_adicional} para que todos los empleados ganen al menos $500.")
