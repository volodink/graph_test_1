import networkx as nx
import pytest
import graph

graph_data = graph.graph_loader('data.txt')
print(graph_data)

nx_graph = graph.get_nx_graph(graph_data)
print(list(nx_graph.nodes))
print(list(nx_graph.edges))

print(nx.shortest_path(nx_graph, source='A', target='D'))
