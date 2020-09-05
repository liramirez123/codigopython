print("Ingrese lo n primeros numero naturales: ")
n = int(input(': '))

suma = n * (n + 1)/2

print("La suma de los n primeros numeros naturales es: ",int(suma))

#-----------------Ejercicio 9------------------------------------------
#Calculo de indice de masa corporal

weight = input("Cual es su peso en kg: ")
height = input("¿Cuál es su estatura en metros: ?")
bmi = round(float(weight)/float(height)**2,2)
print("Su indice de masa corporal es: "+str(bmi))


