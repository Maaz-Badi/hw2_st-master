from Q8 import *


def remove_warehouse(graph, warehouse):
    """
    Removes a warehouses from the supply chain graph, along with its connected supply links.

    If the specified warehouse does not exist in the graph, the function prints an error message. 
    Otherwise, removes the warehouse passed as argument, and all its connections from the graph,
    and the function prints a success message, as specified in the example below.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    warehouse (str): The alphanumeric warehouse ID of the warehouse to be removed.
    
    Returns:
    None

    Example:
    >>> remove_warehouse(G, "W1")
    (W1 has three edges, which will be removed first using remove_supply_link function from 
    the previous question, which will print its success messages, followed by removal of the 
    warehouse W1 itself from the graph, and then prints its success message)
    Supply link removed successfully
    Supply link removed successfully
    Supply link removed successfully
    W1 is successfully removed from the supply chain

    >>> remove_warehouse(G, "W24")
    (Does not modify the graph, and prints a message)
    W24 is not in the supply chain
    """

    # WRITE YOUR CODE HERE
    wh = search_warehouse(graph,warehouse)
    if wh == False:
        print(f'{warehouse} is not in the supply chain')
        return
    
    warehouse_o = None
    for i in graph:
        if i[0] == warehouse:
            warehouse_o = i
            break 

    print(graph[warehouse_o])
    for i in range(len(graph[warehouse_o])):
        d = graph[warehouse_o][0]
        # print(graph[warehouse_o][0])
        remove_supply_link(graph,warehouse,d[0])

    del graph[warehouse_o]
    print(f'{warehouse} is successfully removed from the supply chain')


def main():
    G = create_supply_chain('supply_chain.csv')
    add_supply_link(G, "W1", "W5", (2, 50, "Ground"))
    remove_warehouse(G, "W1")
    """
    Expected Output:
    Supply link removed successfully
    Supply link removed successfully
    Supply link removed successfully
    W1 is successfully removed from the supply chain
    """
     
    remove_warehouse(G, "W24")
    """
    Expected Output:
    W24 is not in the supply chain
    """

if __name__ == "__main__":
    main()
