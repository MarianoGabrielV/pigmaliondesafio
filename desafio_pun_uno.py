# existe una coincidencia.
"""
    Versión 1: Fuerza bruta
    Busca si existe un par de números cuya suma sea igual al objetivo.
    Recorre todos los pares posibles sin optimizar recursos.

    :param lista_numeros: Lista de números enteros
    :param suma_objetivo: Valor objetivo a alcanzar con la suma de dos elementos
    :return: True si existe un par con esa suma, False en caso contrario
"""

def existe_una_coincidencia(lista_numeros, suma_a_llegar):  # Esta funcion toma 2 argumentos, La lista de numeros 
                                                            # y el numero al que hay que llegar
 
    cantidad_a_recorrer = len(lista_numeros) # Calcula la cantidad de elementos de la lista y la guarda en la variable cantidad_a_recorrer.
    for indice_primero in range(cantidad_a_recorrer): # Inicia un bucle que recorre la lista desde el primer elemento (indice_primero). Sirve para tomar uno de los dos números del par.
        for indice_segundo in range(indice_primero + 1, cantidad_a_recorrer):
            primer_numero = lista_numeros[indice_primero]
            segundo_numero = lista_numeros[indice_segundo]
            if primer_numero + segundo_numero == suma_a_llegar:
                return True
    return False


if __name__ == "__main__":
    numeros_ejemplo = [1, 4, 3, 9]
    objetivo = 8
    print(existe_una_coincidencia(numeros_ejemplo, objetivo))  # Esperado: False""

    numeros_ejemplo = [4, 2, 1, 4]
    objetivo = 8
    print(existe_una_coincidencia(numeros_ejemplo, objetivo))  # Esperado: True

    
