#Crea una lista vacía
my_list = []

#Lidta con valores iniciales
my_list = [1,2,3,4,5]

#Acceder a elementos
print (my_list [0]),(my_list[3])

#índice negativo
print (my_list[-1]) #Iniciando desde el último

#Índice que no existe
#print (my_list[5]) #Error

#Sublista
sublista = my_list[3:6] #El último no se toma
print (sublista)

#Dejar vacío el inicio o el final
print (my_list[2 : ]) #hasta el final
print (my_list[ :6]) #Desde el inicio

#Modificar elementos de una lista
#Cambio de valor
my_list [2] = 9
print (my_list)

#Índice que no existe
#my_list [6] = 9

#Agregar elementos a una lista
my_list.append(6)
print(my_list)

#Insertar en una posición
my_list.insert(3,15) #Primero índice, segundo cambio
print(my_list)

#Combinar listas
list2 = [50,60,70]
my_list.extend(list2) #con (): se combinan - con [] lista dentro de la lista
print (my_list)

#Eliminar elementos de una lista
my_list.remove(6)
print (my_list)

#Usar el pop():
my_list.pop(2)
print (my_list)

#Usar Del
del my_list [4] 
print (my_list)

#Buscar elementos dentro de una lista
print (99 in my_list) #Arroja True or Falso

#Obtener índice
print(my_list.index(50)) 

#Contar repeticiones
my_list.append(50) #Agregué número repetido
print(my_list.count(50))

#Ordenar elementos
#Ascendente
print(sorted(my_list)) #Con 'sorted' no se modifica la lista original, sólo la devuelve ordenada ascendentemente
my_list.sort() # con .sort primero la organiza 
print (my_list) #Luego la imprime
#Descendente
my_list.sort(reverse=True) #Ordena la lista en forma descendente
print(my_list)
#Descendente-Revertir con slicing
my_list[::-1] #Duda
print(my_list) 


#Copiar una lista
copia1 = my_list[:] #Con Slicing
copia2 = list(my_list) #Con list
copia3 = my_list.copy() # Con Copy
print(copia1,copia2,copia3)


#Comprobar si una lista está vacía
lista2=[]
if not lista2:
    print("La lista está vacía")
    

#Pedir varios datos al usuaio y almacenarlos
my_list3 = []
n_datos = int(input("Cuántos elemnetos quieres ingresar? "))

for i in range (n_datos): #Bucle for para pedir la cantidad de datos que escribió.
    dato = (input(f"Ingrese el dato # {i+1}: "))
    my_list3.append(dato) #Guardamos el dato en la lista
print("La lista final es: ", my_list3 )
