import divide_and_conqer_db_graph_construction
import basic_db_graph_construction
import pathpy as pp


def convert_pathpy_edges_to_multiset(edges):
    for key in edges:
        # edges[key]['weight'] is an array consisting of two numbers, the number of occurrences of the key in all
        # subpaths and the number of occurrences of the key in all longest paths (I think we need to add them)
        edges[key] = int(sum(edges[key]['weight']))
    return edges


def compare_dictionary_graphs(g1, g2):
    for key in g1:
        if key not in g2 or g1[key] != g2[key]:
            print(key)
            if key in g2:
                print(g1[key])
                print(g2[key])
            return False
    for key in g2:
        if key not in g1 or g1[key] != g2[key]:
            print(key)
            if key in g1:
                print(g1[key])
                print(g2[key])
            return False
    return True


def main():
    # TODO: make the input file a variable/command line argument?
    # Read input path data from the finished paths text file
    # my_file = open("paths_finished.txt", "r")
    my_file = open("basic_path_data", "r")
    path_data = [line.split(';') for line in my_file.read().splitlines()]

    # Create first graph using the basic construction algorithm
    print("Creating baseline graph")
    basic_graph = basic_db_graph_construction.constructDBGraph(path_data, 3)
    print("Finished")
    print()

    # Create second graph using the Divide and Conquer algorithm
    print("Creating graph using Divide and Conquer Algorithm")
    divide_conquer_graph = divide_and_conqer_db_graph_construction.constructDBGraph(path_data, 3)
    print("Finished")
    print()

    # Create the third graph using pathpy
    print("Reading path data from file into Paths object")
    paths = pp.Paths.read_file(filename="paths_finished.txt", separator=';', frequency=False, expand_sub_paths=False)
    # paths = pp.Paths()
    # for path in path_data:
    #     paths.add_path(path, separator=";")
    print("Finished")
    print()

    print(paths)
    print()

    print("Creating HigherOrderNetwork using pathpy")
    pathpy_graph = pp.HigherOrderNetwork(paths, 3)
    print("Finished")
    print()

    # dictionary of edges to compare against the others
    # print(pathpy_graph.edges)
    comparable_pathpy_edges = convert_pathpy_edges_to_multiset(pathpy_graph.edges)

    basic_equals_divide_conquer = compare_dictionary_graphs(basic_graph, divide_conquer_graph)
    basic_equals_pathpy = compare_dictionary_graphs(basic_graph, comparable_pathpy_edges)

    if basic_equals_divide_conquer:
        print("BASIC AND DIVIDE CONQUER ARE THE SAME")
    else:
        print("BASIC AND DIVIDE CONQUER ARE DIFFERENT")

    if basic_equals_pathpy:
        print("BASIC AND PATHPY ARE THE SAME")
    else:
        print("BASIC AND PATHPY ARE DIFFERENT")


if __name__ == "__main__":
    main()