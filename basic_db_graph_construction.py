from typing import List, Dict, Tuple
from collections import deque
import time


def constructDBGraph(s: List[List[str]], k: int) -> Dict[Tuple[str, str], int]:
    g = dict()
    for p in s:
        path_length = len(p)
        if path_length >= k:
            curr_node = deque()
            i = 0
            while i < k:
                curr_node.append(p[i])
                i += 1
            while i < path_length:
                prev_node_str = ';'.join(curr_node)
                curr_node.popleft()
                curr_node.append(p[i])
                curr_node_str = ';'.join(curr_node)
                edge = (prev_node_str, curr_node_str)
                if edge in g:
                    g[edge] += 1
                else:
                    g[edge] = 1
                i += 1
    return g


def main():
    start_time = time.time()
    my_file = open("paths_finished.txt", "r")
    path_data = [line.split(';') for line in my_file.read().splitlines()]
    end_time = time.time()
    print("Read file in " + str(round(end_time - start_time, 2)) + " seconds")

    start_time = time.time()
    e = constructDBGraph(path_data, 3)
    end_time = time.time()
    print("Constructed graph in " + str(round(end_time - start_time, 2)) + " seconds")
    print(dict(list(e.items())[0: 10]))


if __name__ == "__main__":
    main()
