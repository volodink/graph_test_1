import networkx as nx
import graph


def test_check_shortest_path():
    # load data
    graph_data = graph.graph_loader('data.txt')

    # create graph
    nx_graph = graph.get_nx_graph(graph_data)
    my_graph = graph.get_my_graph(graph_data)

    # get shortest_path
    expected_path = nx.shortest_path(nx_graph, source='A', target='D')
    my_path = graph.my_shortest_path(my_graph, 'A', 'D')

    assert my_path == expected_path
