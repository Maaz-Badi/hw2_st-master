from Q9 import *
from stack import *

def count_all_supply_chain_connections(graph, warehouse_o, warehouse_i):
    """
    Finds the count of all connections between the origin and the destination warehouses using DFS.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    warehouse_o (str): The alphanumeric warehouse ID of the origin vertex.
    warehouse_i (str): The alphanumeric warehouse ID of the destination vertex.

    Returns:
    int: The count of all paths connecting the two warehouses. 
    If there is no such warehouse in the graph, it returns None
    If both warehouse_o and warehouse_i refer to the same warehouse, then the count should be 0
    """

    # WRITE YOUR CODE HERE
    wo = search_warehouse(graph,warehouse_o)
    wi = search_warehouse(graph, warehouse_i)
    if wo == False or wi == False:
        return None
    if warehouse_o == warehouse_i:
        return 0
    
    stack = [(warehouse_o, set([warehouse_o]))]
    count = 0

    while stack:
        current_node_name, visited = stack.pop()

        if current_node_name == destination_name:
            count += 1
            continue

        for node_key, neighbors in graph.items():
            if node_key[0] == current_node_name:
                for (neighbor_name, *_rest) in neighbors:
                    if neighbor_name not in visited:
                        stack.append((neighbor_name, visited | {neighbor_name}))

    return count

    


def main():
    G = create_supply_chain('supply_chain.csv')
    print(count_all_supply_chain_connections(G, "W4", "W10"))
    """ Expected Output: 16148 """

    print(count_all_supply_chain_connections(G, "W1", "W11"))
    """ Expected Output: 74597 """
    
    print(count_all_supply_chain_connections(G, "W4", "W4"))
    """ Expected Output: 0 """
    
    print(count_all_supply_chain_connections(G, "W24", "W10"))
    """ Expected Output: None """


if __name__ == "__main__":
    main()
