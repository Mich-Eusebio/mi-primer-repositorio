# Palabra de prueba
palabra = "amor"

# Función para comprobar palíndromos
def is_paronimo(n):
    # Caso base: si la longitud es 0 o 1, es un palíndromo
    if n <= 1:
        return palabra[n-1]

    # Construir la palabra inversa utilizando la recursividad
    palabra_inversa = palabra[n-1] + is_paronimo(n-1)

    # Devolver la palabra inversa
    return palabra_inversa

# Comparar la palabra original con la palabra inversa
if palabra == is_paronimo(len(palabra)):
    print("Sí es un palíndromo.")
else:
    print("No es un palíndromo.")
