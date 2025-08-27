import os
from queue import Queue

# Ruta de la carpeta raíz
RAIZ = "animales"

# Renombrar funciones para mayor claridad
obtener_nombre = os.path.basename
listar_elementos = os.listdir
unir_rutas = os.path.join
es_carpeta = os.path.isdir

# =========================
# DFS - recursivo
def recorrer_dfs(ruta):
    if es_carpeta(ruta):
        print(f"📁 {obtener_nombre(ruta)}")  # Carpeta
        for elemento in listar_elementos(ruta):
            recorrer_dfs(unir_rutas(ruta, elemento))
    else:
        print(f"📄 {obtener_nombre(ruta)}")  # Archivo

# =========================
# BFS - iterativo con cola
def recorrer_bfs(ruta):
    cola = Queue()
    cola.put(ruta)

    while not cola.empty():
        actual = cola.get()
        if es_carpeta(actual):
            print(f"📁 {obtener_nombre(actual)}")  # Carpeta
            for elemento in listar_elementos(actual):
                cola.put(unir_rutas(actual, elemento))
        else:
            print(f"📄 {obtener_nombre(actual)}")  # Archivo

# ===========================
print("=== RECORRIDO DFS ===")
recorrer_dfs(RAIZ)

print("\n=== RECORRIDO BFS ===")
recorrer_bfs(RAIZ)
