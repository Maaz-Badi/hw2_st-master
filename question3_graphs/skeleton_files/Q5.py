from Q4 import *

def get_cheapest_outgoing_supply_route(graph, wh):
    """
    Finds the cheapest outgoing supply route from a given warehouse.

    This function searches for all outgoing connections from the given warehouse
    and determines the route with the lowest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the origin warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the cheapest outgoing supply route.
    None: If the warehouse has no outgoing supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    warehouse = None
    for i in graph:
        if i[0] == wh:
            warehouse = i
            break
    if warehouse == None:
        return None
    if graph[warehouse] == []:
        return None
    minimum = 10000000
    edge = None
    for i in graph[warehouse]:
        a,b =  i
        t,c,m = b
        # print (c)
        if c < minimum:
            minimum = c
            edge = i

        
    return(wh,edge[0])



    
    
    
            
def get_cheapest_incoming_supply_route(graph, wh):
    """
    Finds the cheapest incoming supply route for a given warehouse.

    This function searches for all incoming connections to the given warehouse
    and determines the route with the lowest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the destination warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the cheapest incoming supply route.
    None: If the warehouse has no incoming supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    warehouse = None
    for i in graph:
        if i[0] == wh:
            warehouse = i
            break
    if warehouse == None:
        return None
    P = []
    for i in graph:
        for j in graph[i]:
            if j[0] == wh:
                P.append((j,i))
    # print(P)
    minimum = 10000000
    edge = None
    for i in P:
        a,b = i
        q,w = a
        t,c,m = w
        if c<minimum:
            minimum = c
            edge = b[0]
    
    if edge == None:
        return edge
    return(edge,wh)
    

def get_expensive_outgoing_supply_route(graph, wh):
    """
    Finds the most expensive outgoing supply route from a given warehouse.

    This function searches for all outgoing connections from the given warehouse
    and determines the route with the highest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the origin warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the most expensive outgoing supply route.
    None: If the warehouse has no outgoing supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    warehouse = None
    for i in graph:
        if i[0] == wh:
            warehouse = i
            break
    if warehouse == None:
        return None
    max = 0
    edge = None
    for i in graph[warehouse]:
        a , b =  i
        t,c,m = b
        if c > max:
            max = c
            edge = i
        
    return(wh,edge[0])
            
def get_expensive_incoming_supply_route(graph, wh):
    """
    Finds the most expensive incoming supply route for a given warehouse.

    This function searches for all incoming connections to the given warehouse
    and determines the route with the highest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the destination warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the most expensive incoming supply route.
    None: If the warehouse has no incoming supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    warehouse = None
    for i in graph:
        if i[0] == wh:
            warehouse = i
            break
    if warehouse == None:
        return None    
    P = []
    for i in graph:
        for j in graph[i]:
            if j[0] == wh:
                P.append((j,i))
    # print(P)
    max = 0
    edge = None
    for i in P:
        a,b = i
        q,w = a
        t,c,m = w
        if c>max:
            max = c
            edge = b[0]
    
    if edge == None:
        return edge
    return(edge,wh)
    

def main():
    G = create_supply_chain('supply_chain.csv')
 
    route = get_cheapest_outgoing_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W14', 'W17')
    """
    
    route = get_cheapest_outgoing_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_expensive_outgoing_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W14', 'W1')
    """

    route = get_expensive_outgoing_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_cheapest_incoming_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W16', 'W14')
    """

    route = get_cheapest_incoming_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_expensive_incoming_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W18', 'W14')
    """

    route = get_expensive_incoming_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

if __name__ == "__main__":
    main()
