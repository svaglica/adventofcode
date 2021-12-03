import networkx as nx

with open('./orbits.txt') as f:
    orbits = f.read().splitlines()

for i in range(len(orbits)):
    orbits[i] = orbits[i].split(')')

orbits_tree = nx.Graph()

for edge in orbits:
    orbits_tree.add_edge(edge[0], edge[1])

orbits_total = 0
for node in orbits_tree.nodes():
    orbits_total += nx.shortest_path_length(orbits_tree, 'COM', node)

print(orbits_total)
print(nx.shortest_path_length(orbits_tree, 'YOU', 'SAN') -2)
