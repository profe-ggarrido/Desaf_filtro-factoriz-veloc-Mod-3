#DESAFIO SOBRE FILTROS RELEVANTES
# ---------------------------------

#CONTROL DE TERMINAL LIMPIA
import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
limpiar_consola()

precios = {'Notebook': 700000, 
    'Teclado': 25000, 
    'Mouse': 12000, 
    'Monitor': 250000, 
    'Escritorio': 135000, 
    'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral):
    #RECORRER EL DICC PARA VALORES SEGÙN EL UMBRAL
    #---------------------------------------------
    filtro = {k:v for k, v in diccionario.items() if v == umbral}
    return filtro

#ENVIAR A CONSOLA LOS ARTICULOS IGUALES A $12.000
# print(f"umbral: {umbral}")

print("\033[42m**************************************************************\033[0m")
print("elementos cuyo precio es \033[1migual al umbral de 12.000\033[0m")
print(filtrar(precios,12000))
print("")


def filtrar(diccionario, umbral):
    #RECORRER EL DICC PARA VALORES SEGÙN ELSEGUNDO UMBRAL
    #---------------------------------------------------
    filtro = {k:v for k, v in diccionario.items() if v > umbral}
    return filtro

#OBTENER POR CONSOLA LOS ARTICULOS MAYORES  A $200.000
print("elementos cuyo precio es MAYOR al umbral de $200.000")
print(filtrar(precios,200000))
print("")
print("\033[41m**************************************************************\033[0m")



