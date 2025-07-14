
# IMPORTANTE LEER EL README.md PREVIO A SU UTILIZACION https://github.com/MarianoGabrielV/pigmaliondesafio
# existe_una_coincidencia

"""
    Versión 1: Fuerza bruta
    Verifica si existe al menos un par de numeros en la lista cuya suma sea igual al numero solicitado.
    Recorre todos los pares posibles de la lista sin optimizacion, utilizando dos bucles anidados.

    Parametros:
    lista_numeros: Lista de numeros enteros
    suma_a_llegar: Numero que se desea alcanzar sumando dos elementos de la lista
    True: Si existe al menos un par con esa suma.
    False: En caso contrario.
"""

def existe_una_coincidencia(lista_numeros, suma_a_llegar):
    cantidad_elementos = len(lista_numeros)  # Cantidad total de elementos en la lista

    for indice_primero in range(cantidad_elementos):
        for indice_segundo in range(indice_primero + 1, cantidad_elementos): # Se toman los dos numeros correspondientes a las posiciones actuales
            primer_numero = lista_numeros[indice_primero]
            segundo_numero = lista_numeros[indice_segundo]

            if primer_numero + segundo_numero == suma_a_llegar:
                return True # Si encontramos un par que sume el numero al cual queremos llegar, retornara True

    return False # Si se recorren todos y no hay coincidencias, retornara False


# Ejemplos de uso para verificar el correcto funcionamiento
if __name__ == "__main__":
    numeros_ejemplo = [1, 4, 3, 9]
    objetivo = 8
    print(existe_una_coincidencia(numeros_ejemplo, objetivo))  # Esperado: False

    numeros_ejemplo = [4, 2, 1, 4]
    objetivo = 8
    print(existe_una_coincidencia(numeros_ejemplo, objetivo))  # Esperado: True
