# # Approximations and Heuristics
# Approximations of graph properties and Heuristic methods for optimization.

# # import
# These functions can be accessed using networkx.approximation.function_name

# They can be imported using from networkx.algorithms import approximation or from networkx.algorithms.approximation import function_name

# # Treewidth
# Functions for computing treewidth decomposition.

# Treewidth of an undirected graph is a number associated with the graph. It can be defined as the size of the largest vertex set (bag) in a tree decomposition of the graph minus one.

# Wikipedia: Treewidth

# treewidth_min_degree(G): Returns a treewidth decomposition using the Minimum Degree heuristic.


from networkx.algorithms import approximation as algos
algos.treewidth_min_degree(G)