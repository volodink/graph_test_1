import networkx as nx


# (('A', 'B', 'C'), [('A', 'B'), ('B', 'C')])
def graph_loader(graph_file):
    with open(graph_file, 'r') as gfile:
        nodes = tuple(gfile.readline().rstrip())
        edges = [tuple(e.rstrip()) for e in gfile]
    return nodes, edges


def get_nx_graph(graph_data):
    graph = nx.Graph()

    for node in graph_data[0]:
        graph.add_node(node)

    for u, v in graph_data[1]:
        graph.add_edge(u, v)

    return graph


def get_my_graph(graph_data):
    g = dict()

    return g


def my_shortest_path(my_graph, param, param1):
    return None
