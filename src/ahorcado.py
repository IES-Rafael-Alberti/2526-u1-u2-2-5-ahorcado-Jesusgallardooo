"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: Jesús Gallardo Domínguez
Fecha: 6/11/2025
"""

EQUIVALENCIAS_TILDES = { # 10 elementos para que sea bidireccional. 
    "Á": "A", "A": "Á",
    "É": "E", "E": "É",
    "Í": "I", "I": "Í",
    "Ó": "O", "O": "Ó",
    "Ú": "U", "U": "Ú"
} 

def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)


def solicitar_palabra()-> str:
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns:
        str: La palabra a adivinar en mayúsculas
    """

    palabra = input("Introduzca la palabra que tiene en mente --> ").upper()

    while (not palabra.isalpha()) or (len(palabra) < 5) :
        print("valor introducido incorrecto, tiene que tener +5 caracteres y solo puede contener letras.")
        palabra = input("Introduzca la palabra que tiene en mente --> ").upper()
        
    return palabra


def solicitar_letra(letras_usadas:list)-> str:
    """
    Solicita una letra al jugador 2.
    La letra debe ser válida (solo una letra) y no estar ya usada.

    Parameters
    ----------
    letras_usadas : list
        Lista de letras ya introducidas.

    Returns
    -------
    str
        La letra introducida en mayúsculas.
    """

    letra = input("Introduzca la letra que tiene en mente --> ").upper()
    print()

    while (len(letra) != 1) or (not letra.isalpha()) or (letra in letras_usadas):

        if letra in letras_usadas:
            print("letra ya registrada, prueba otra vez.")
        else:
            print("valor introducido inválido, solo puede introducir letras individualmente, prueba otra vez.")
        
        letra = input("Introduzca la letra que tiene en mente --> ").upper()
        print()

    return letra


def mostrar_estado(palabra_oculta:str, intentos:int, letras_usadas:list):
    """
    Muestra el estado actual del juego.

    :param palabra_oculta: La palabra con guiones bajos y letras adivinadas.
    :type palabra_oculta: str
    :param intentos: Número de intentos restantes.
    :type intentos: int
    :param letras_usadas: Lista de letras ya usadas.
    :type letras_usadas: list
    """
    
    print(f"Intentos restantes --> {intentos}\n")
    print(" ".join(palabra_oculta))

    if letras_usadas:
        print("\nLetras usadas -->", " ".join(letras_usadas) + "\n")
    else:
        print("\nAún no has usado ninguna letra.\n")



def actualizar_palabra_oculta(palabra:str, palabra_oculta:str, letra:str)-> str:
    # Actualiza la palabra oculta revelando las apariciones de la letra.
    #
    # Parámetros:
    #   palabra (str): La palabra completa a adivinar.
    #   palabra_oculta (str): La palabra actual con guiones bajos y letras adivinadas.
    #   letra (str): La letra que se ha adivinado.
    #
    # Devuelve:
    #   str: La palabra oculta actualizada.

    palabra_oculta =  list(palabra_oculta)

    for i, caracter in enumerate(palabra):
        if caracter == letra or EQUIVALENCIAS_TILDES.get(caracter) == letra:
            palabra_oculta[i] = caracter

    return "".join(palabra_oculta)



def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")
    
    INTENTOS_MAXIMOS = 5
    palabra = solicitar_palabra()

    limpiar_pantalla()
    
    palabra_oculta = "_" * len(palabra)
    intentos = INTENTOS_MAXIMOS
    letras_usadas = []
    juego_terminado = False
    
    print("Jugador 2: ¡Adivina la palabra!\n")

    while (intentos > 0) and (juego_terminado == False):
    
        mostrar_estado(palabra_oculta, intentos, letras_usadas)

        letra = solicitar_letra(letras_usadas)

        letras_usadas.append(letra)

        if letra in palabra or EQUIVALENCIAS_TILDES.get(letra, "") in palabra:
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            print(" <<< ACIERTO >>> \n")

            if "_" not in palabra_oculta:
                juego_terminado = True 
                print(" <<< ¡¡¡ HAS GANADO !!! >>> \n")

        if letra not in palabra and EQUIVALENCIAS_TILDES.get(letra, "") not in palabra:  
            intentos -= 1      
            print("<<< FALLO... >>> \n")
    
    if juego_terminado:
        print(f" ¡¡¡ FELICIDADES, HAS ADIVINADO LA PALABRA !!! --> {palabra} \n")
    else:
        print(f"DERROTA, otra vez será... la palabra era --> {palabra} \n")


def main():
    """
    Punto de entrada del programa
    """
    jugar()
    
    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() == 's':
        main()


if __name__ == "__main__":
    main()
