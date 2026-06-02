# Grafo representado como diccionario de adyacencia

grafo = {
    "casa": {
        "parque": 2,
        "tienda": 5
    },
    "parque": {
        "casa": 2,
        "tienda": 1,
        "escuela": 4
    },
    "tienda": {
        "casa": 5,
        "parque": 1,
        "cine": 3
    },
    "escuela": {
        "parque": 4,
        "cine": 1
    },
    "cine": {
        "tienda": 3,
        "escuela": 1
    }
}

inicio = "casa"
destino = "cine"

# Distancias iniciales
distancias = {}

for nodo in grafo:
    distancias[nodo] = float('inf')

distancias[inicio] = 0

# Para reconstruir la ruta
anteriores = {}

# Nodos sin visitar
no_visitados = list(grafo.keys())

while no_visitados:

    # Buscar nodo con menor distancia
    nodo_actual = min(
        no_visitados,
        key=lambda nodo: distancias[nodo]
    )

    no_visitados.remove(nodo_actual)

    # Revisar vecinos
    for vecino, peso in grafo[nodo_actual].items():

        nueva_distancia = distancias[nodo_actual] + peso

        if nueva_distancia < distancias[vecino]:
            distancias[vecino] = nueva_distancia
            anteriores[vecino] = nodo_actual

# Reconstrucción de la ruta
ruta = []
actual = destino

while actual != inicio:
    ruta.append(actual)
    actual = anteriores[actual]

ruta.append(inicio)
ruta.reverse()

print("Ruta más corta:", ruta)
print("Costo total:", distancias[destino])