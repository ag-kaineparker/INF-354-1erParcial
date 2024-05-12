from kanren import Relation, facts, var, run
import networkx as nx
import matplotlib.pyplot as plt

# Definir variables lógicas
persona = var()
pariente = var()

# Crear relaciones
padre = Relation()
madre = Relation()
tia = Relation()
hermano = Relation()
primo = Relation()

# Establecer hechos
facts(padre, ("Fabio", "Yo"), ("Fabio", "Mai"), ("Fabio", "Mary"), ("Fabio", "Naomi"), ("Fabio", "Johann"),
      ("Raul", "Gherald"), ("Raul", "Estefania"))
facts(madre, ("Ana", "Fabio"), ("Ana", "Gilda"), ("Ana", "Reyna"),
      ("Gilda", "Gherald"), ("Gilda", "Estefania"),
      ("Reyna", "Nayeli"))
facts(tia, ("Gilda", "Yo"), ("Gilda", "Mai"), ("Gilda", "Mary"), ("Gilda", "Naomi"), ("Gilda", "Johann"),
      ("Reyna", "Gherald"), ("Reyna", "Estefania"))
facts(hermano, ("Yo", "Mai"), ("Yo", "Mary"), ("Yo", "Naomi"), ("Yo", "Johann"))
facts(primo, ("Mai", "Gherald"), ("Mai", "Estefania"), ("Mary", "Gherald"), ("Mary", "Estefania"),
      ("Naomi", "Gherald"), ("Naomi", "Estefania"), ("Johann", "Gherald"), ("Johann", "Estefania"))

# Definir relaciones
relaciones = [("Ana", "Fabio"), ("Ana", "Gilda"), ("Ana", "Reyna"),
              ("Fabio", "Yo"), ("Fabio", "Mai"), ("Fabio", "Mary"), ("Fabio", "Naomi"), ("Fabio", "Johann"),
              ("Gilda", "Gherald"), ("Gilda", "Estefania"),
              ("Reyna", "Nayeli")]
print("Ejemplo de relaciones: ")
# Imprimir los hechos para la relación "padre"
for nombre_hijo in ["Yo", "Mai", "Mary", "Naomi", "Johann"]:
    padre_facts = run(1, persona, padre(persona, nombre_hijo))
    print(f"Padre de {nombre_hijo}:")
    print(padre_facts)

# Imprimir los hechos para la relación "madre"
for nombre_hijo in ["Yo", "Mai", "Mary", "Naomi", "Johann"]:
    madre_facts = run(1, persona, madre(persona, nombre_hijo))
    if madre_facts:
        print(f"Madre de {nombre_hijo}:")
        print(madre_facts[0])

# Imprimir los hechos para la relación "tia"
for nombre_sobrino in ["Yo", "Mai", "Mary", "Naomi", "Johann"]:
    tia_facts = run(1, persona, tia(persona, nombre_sobrino))
    print(f"Tía de {nombre_sobrino}:")
    print(tia_facts)

# Imprimir los hechos para la relación "hermano"
for nombre_hermano in ["Mai", "Mary", "Naomi", "Johann"]:
    hermano_facts = run(0, persona, hermano(persona, nombre_hermano))
    print(f"Hermano de {nombre_hermano}:")
    print(hermano_facts)

# Imprimir los hechos para la relación "primo"
for nombre_primo in ["Gherald", "Estefania"]:
    primo_facts = run(0, persona, primo(persona, nombre_primo))
    print(f"Primo de {nombre_primo}:")
    print(primo_facts)


# Crear un gráfico dirigido
G = nx.DiGraph()

# Agregar nodos y relaciones al gráfico
for madre, hijo in relaciones:
    G.add_edge(madre, hijo)



# Dibujar el gráfico con etiquetas de bordes
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Árbol Genealógico")
plt.show()
