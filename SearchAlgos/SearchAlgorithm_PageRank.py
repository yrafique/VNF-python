# Page Rank Algorithm
#Ranking nodes based on various strategies is a common thing in measuring node importance. PageRank is one of the most successful one and has still been used in both the industry and academia. 
#Usually, PageRank is applied in a directed network, where an edge has a direction. For example, webpage A has a link to webpage B but not the other way around. 
#Therefore in the network of WWW, we only have A → B but NOT B → A.

## Reference:
#Page, Lawrence and Brin, Sergey and Motwani, Rajeev and Winograd, Terry (1999) The PageRank Citation Ranking: Bringing Order to the Web. Technical Report. Stanford InfoLab.

## Build network
#Network data from http://tuvalu.santafe.edu/~aaronc/datacode.htm

import networkx as nx
import pandas as pd

def compute_pagerank(G):
    """
    Calculate the PageRank values for the nodes in the input graph G.

    Parameters:
    G: networkx.Graph
        The input graph

    Returns:
    pr_df_sorted: pandas.DataFrame
        DataFrame containing nodes and their corresponding PageRank values, sorted in descending order
    """

    # Calculate the PageRank of the nodes in the graph G
    # alpha is the damping factor, usually set to 0.85
    # The PageRank algorithm measures the importance of nodes in a graph based on the structure of incoming links
    pr = nx.pagerank(G, alpha=0.85)

    # Convert the PageRank dictionary into a pandas DataFrame
    # The DataFrame will have two columns: 'name' for the node identifier and 'value' for the PageRank value
    pr_df = pd.DataFrame([{'name': k, 'value': v} for k, v in pr.items()])

    # Sort the DataFrame by the 'value' column (PageRank value) in descending order
    # This will show the nodes with the highest PageRank values at the top
    pr_df_sorted = pr_df.sort_values('value', ascending=False)

    return pr_df_sorted

