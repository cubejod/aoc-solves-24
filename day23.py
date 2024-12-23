# decently fast today with copy pasting clique algorithms. this networkx stuff is crazy though so i rewrote my code with it for practice
import networkx as nx
l = open("day23input.txt").read().strip().split("\n")
op, op2 = 0, 0
G = nx.Graph()

for line in l:
    a, b = line.split("-")
    G.add_edge(a, b)
    pass

cliques = list(nx.enumerate_all_cliques(G))

for i in range(len(cliques)):
    if len(cliques[i]) == 3:
        for j in range(len(cliques[i])):
            if cliques[i][j][0] == "t":
                op += 1
                break

max_clique = sorted(max(cliques, key=len))
op2 = (','.join(max_clique))
print(op)
print(op2)
