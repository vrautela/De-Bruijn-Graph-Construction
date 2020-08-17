from typing import List, Dict, Tuple
from collections import Counter, deque
import time


def combine_graphs(e_1: Dict[Tuple[str, str], int], e_2: Dict[Tuple[str, str], int]) -> Dict[Tuple[str, str], int]:
    for key in e_1:
        if key in e_2:
            e_2[key] += e_1[key]
        else:
            e_2[key] = e_1[key]
    return e_2


def constructDBGraph(s: List[List[str]], k: int) -> Dict[Tuple[str, str], int]:
    if len(s) == 1:
        return constructGraphFromPath(s[0], k)
    else:
        mid = len(s) // 2
        e_1 = constructDBGraph(s[:mid], k)
        e_2 = constructDBGraph(s[mid:], k)

        return combine_graphs(e_1, e_2)


def constructGraphFromPath(p: List[str], k: int) -> Dict[Tuple[str, str], int]:
    e = dict()
    path_length = len(p)
    if path_length < k:
        return e
    else:
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
            # Do we need to have a hash of the edge, or can the key be the edge itself?
            # edge_hash = hash(edge)
            # if edge_hash in e:
            #     e[edge_hash] += 1
            # else:
            #     e[edge_hash] = 1
            if edge in e:
                e[edge] += 1
            else:
                e[edge] = 1
            i += 1
    return e


def main():
    start_time = time.time()
    my_file = open("paths_finished.txt", "r")
    path_data = [line.split(';') for line in my_file.read().splitlines()]
    end_time = time.time()
    print("Read file in " + str(round(end_time - start_time, 2)) + " seconds")
    print(path_data[:10])

    start_time = time.time()
    e = constructDBGraph(path_data, 3)
    end_time = time.time()
    print("Constructed graph in " + str(round(end_time - start_time, 2)) + " seconds")
    print(dict(list(e.items())[0: 10]))


if __name__ == "__main__":
    main()
