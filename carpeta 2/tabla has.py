class Tablahash:
    def __init__(self, tamaño):
        self.tamaño =tamaño
        self.tabla = {}

    def indice(self, key):
        return hash(key)% self.tamaño

    def agregar(self, value):
        clave = sum(list(map(ord, value)))
        self.tabla[clave] = value

    def buscar(self, clave):
        return self.tabla.get(clave, "No existe esta clave")

tabla = Tablahash(10)
books = [
    "The Little Prince",
    "The Old Man and the Sea",
    "The Little Memaid",
    "Beauty and the Beast",
    "The Last Leaf",
    "Alice in Wonderland",
]

for book in books:
    tabla.agregar(book)
print(len(tabla.tabla))
for clave, libro in tabla.tabla.items():
    print(clave, libro)