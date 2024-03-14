#LISTA PROPORCIONADA por lms
# SE USAN VARIALES RELACIONADAS A LOS PROCESOS PARA MAYOR CLARIDAD

velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16,
  10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9,  18, 4, 18, 
  1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 
  5, 23, 3, 5, 9, 5,  3, 12, 20, 5, 11, 10, 18, 10, 14, 
  5, 23,  20, 23, 21]

# Calcular el promedio de los elementos en la lista
promedio = sum(velocidad) / len(velocidad)

# Lista para almacenar las posiciones de los elementos que están por encima del promedio
posiciones_por_encima_promedio = [] # SE CREA LISTA VACIA COMO LA DE LA CLASE CON MIS DATOS

# Contador para contar los elementos que están por encima del promedio
contador_por_encima_promedio = 0

# Recorrer la lista y contar los elementos que están por encima del promedio
for i, elemento in enumerate(velocidad):
    if elemento > promedio:
        contador_por_encima_promedio += 1
        posiciones_por_encima_promedio.append(i)

# Imprimir el número de elementos por encima del promedio
print(f"Número de elementos por encima del promedio: {contador_por_encima_promedio}")

# Imprimir la lista de posiciones por encima del promedio
print("Posiciones de los elementos por encima del promedio:")
print(posiciones_por_encima_promedio)
print("******** GAME OVER *********")

