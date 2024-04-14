# añdiendo cambios para aprender sobre git
print("este método de búsqueda es muy lento")

ciudades = [
    "Daca, Bangladés",
    "Karachi, Pakistán",
    "Nueva Delhi, India",
    "Manila, Filipinas",
    "Seúl, Corea del Sur",
    "Cantón, China",
    "Taipéi, Taiwán",
    "Chenaral, Chile",
    "Shenzhen, China",
    "Bombay, India"
]

def obtener_posicion(ciudades, ciudad):
        if ciudad in ciudades:
            posición = ciudades.index(ciudad)
            return posición            
        else:
            raise ValueError("No se encontró el elemento")


posicion_ocupada = obtener_posicion(ciudades,"Seúl, Corea del Sur")        
print("El elemento está en la posición ", posicion_ocupada)