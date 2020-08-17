import divide_and_conqer_db_graph_construction
import basic_db_graph_construction
import time
import pathpy as pp


def main():
    start_time = time.time()
    my_file = open("paths_finished.txt", "r")
    path_data = [line.split(';') for line in my_file.read().splitlines()]
    end_time = time.time()
    print("Read file in " + str(round(end_time - start_time, 2)) + " seconds")
    print(path_data[:10])

    K = 10

    # constructing each of the models from orders 1-10 using a basic method
    basic_models = []
    start_time = time.time()
    for k in range(1, K+1):
        basic_models.append(basic_db_graph_construction.constructDBGraph(path_data, k))
    end_time = time.time()
    print("Basic: Constructed " + str(K) + "th order graph in " + str(round(end_time - start_time, 2)) + " seconds")

    # constructing each of the models from order 1-10 using divide and conquer
    dc_models = []
    start_time = time.time()
    for k in range(1, K+1):
        dc_models.append(divide_and_conqer_db_graph_construction.constructDBGraph(path_data, k))
    end_time = time.time()
    print("Divide and Conquer: Constructed " + str(K) + "th order graph in " + str(round(end_time - start_time, 2)) + " seconds")

    # constructing a higher order network with all models of order 1-10 using pathpy
    start_time = time.time()
    # paths = pp.Paths()
    # for path in path_data:
    #     paths.add_path(path, separator=";")
    paths = pp.Paths.read_file(filename="paths_finished.txt", separator=';', frequency=False, expand_sub_paths=False)
    end_time = time.time()
    print("Pathpy: Read file in " + str(round(end_time - start_time, 2)) + " seconds")

    # pathpy
    start_time = time.time()
    pathpy_graph = pp.HigherOrderNetwork(paths, K)
    end_time = time.time()
    print("Pathpy: Constructed " + str(K) + "th order graph in " + str(round(end_time - start_time, 2)) + " seconds")


if __name__ == "__main__":
    main()
