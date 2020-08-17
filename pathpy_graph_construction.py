import pathpy as pp
import time


# paths = pp.Paths.read_file(filename="paths_finished.txt", separator=';', frequency=False, expand_sub_paths=False)
paths = pp.Paths.read_file(filename="paths_finished.txt", separator=';', frequency=False, expand_sub_paths=False)
start_time = time.time()
graph = pp.HigherOrderNetwork(paths, 3)
end_time = time.time()

print("Running time of pathpy: " + str(round(end_time - start_time, 2)) + " seconds")

print(dict(list(graph.edges.items())))