import matplotlib.pyplot as plt
import networkx as nx

Grafo = nx.Graph()
Grafo.add_edge("casa","parque", weight = 2)
Grafo.add_edge("casa","tienda", weight = 5)
Grafo.add_edge("parque","tienda", weight = 1)
Grafo.add_edge("parque","escuela", weight = 4)
Grafo.add_edge("tienda","cine", weight = 3)
Grafo.add_edge("escuela","cine", weight = 1)

inicio = "casa"
destino = "cine"

ruta_mas_corta = nx.dijkstra_path(Grafo, source = inicio, target = destino, weight= "weight" )
longitud_ruta = nx.dijkstra_path_length(Grafo, source = inicio, target = destino, weight= "weight" )

print("Ruta: ", ruta_mas_corta)
print("Distancia: ", longitud_ruta)

plt.figure(figsize=(8,6))
pos = nx.spring_layout(Grafo)

ruta_edges = list(zip(ruta_mas_corta, ruta_mas_corta[1:]))

nx.draw(Grafo ,
     pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue"
)

nx.draw_networkx_edges(
   Grafo,
   pos,
   edgelist= ruta_edges,
   edge_color="red",
   width = 4 
)

labels = nx.get_edge_attributes( Grafo, "weight")
nx.draw_networkx_edge_labels(
    Grafo,
    pos,
    edge_labels= labels
)

plt.show()


