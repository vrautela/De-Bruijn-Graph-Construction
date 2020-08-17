# De-Bruijn-Graph-Construction
Scripts for creating a De Bruijn graph given path data

This repository contains three scripts which can be used to create a De Bruijn graph: 
- basic_db_graph_construction.py, 
- divide_and_conquer_db_graph_construction.py, 
- pathpy_graph_construction.py

The input to each of these scripts must be a text file where each path is separated by a newline and each path consists of nodes separated by a ';'.
The output of the first two scripts is a dictionary where the key is an edge in the graph and its value is its weight. The output of the third script is 
a HigherOrderNetwork which is an object in the Pathpy library (https://github.com/IngoScholtes/pathpy)
