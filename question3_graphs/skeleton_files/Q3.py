from Q2 import *

def list_of_incident_edges(G, wh):
    """
        Retrieves the list of edges incident to a given warehouse in the supply chain graph.

        An incident edge is an edge that has the given warehouse as either its source or destination.

        Parameters:
        G (dict): The supply chain graph represented as an adjacency map.
        wh (str): The alphanumeric warehouse ID for which incident edges are being retrieved.

        Returns:
        list: A list of tuples representing incident edges in the format:
            (origin_warehouse, destination_warehouse, shipment_time, shipment_cost, shipping_method).
            If no incident edges exist, the function returns an empty list.
    """

    # WRITE YOUR CODE HERE
    veritce = None
    P = []
    for i in G:
        if i[0] == wh:
            veritce = i
            break
    if veritce == None:
        return P
    for i in G[veritce]:
        q,w = i
        a,b,c = w
        P.append((veritce,q,a,b,c))
    return P


def is_connected(graph, warehouse_o, warehouse_i):
    """
        Checks if there is a direct connection between two warehouses in the supply chain graph.

        This function determines whether an outbound shipment exists from the origin warehouse to 
        the destination warehouse. Remember, a shipment cannot originate and end at the same warehouse, 
        so that connection will be considered False

        Parameters:
        graph (dict): The supply chain graph represented as an adjacency map.
        warehouse_o (str): The alphanumeric warehouse ID of the origin vertex.
        warehouse_i (str): The alphanumeric warehouse ID of the destination vertex.

        Returns:
        bool: True if there is a direct connection from warehouse_o to warehouse_i, False otherwise.

        Example:
        >>> is_connected(G, "W1", "W11")
            (Warehouse, W1 has an outgoing connection to W11)
            True
    
        >>> is_connected(G, "W1", "W15")
            (Warehouse, W1 has no outgoing connection with W15)
            False

        >>> is_connected(G, "W1", "W1") 
            (A warehouse cannot ship anything to itself, so it returns False)
            False
    """

    # WRITE YOUR CODE HERE
    Q = list_of_incident_edges(graph,warehouse_o)
    if warehouse_o == warehouse_i:
        return False
    con = False
    for i in Q:
        if i[1] == warehouse_i:
            con = True

    return con

def if_disconnected(graph, warehouse_o, warehouse_i):
    """
        Finds the fastest alternate shipping route between two warehouses even if the direct connection is available.

        This function first checks if there is a direct connection between the origin and destination warehouse.
        If the direct connection exists, it finds an alternative route using the same shipping method but 
        with the shortest shipment time.

        Parameters:
        graph (dict): The supply chain graph represented as an adjacency map.
        warehouse_o (str): The alphanumeric warehouse ID of the origin vertex.
        warehouse_i (str): The alphanumeric warehouse ID of the destination vertex.

        Returns:
        tuple: A list of tuples representing the fastest alternate edge in the format:
            (origin_warehouse, destination_warehouse, shipment_time, shipment_cost, shipping_method).
            Returns None if either of the origin or destination warehouses do not exist.
            Returns -1 if no alternate edge exists.

        >>> if_disconnected(G, "W15", "W5")
            (Shipment Method between W15 and W5 is via Sea, so if we remove this connection, the next faster Sea shipment
              from W15 is via W19, so it selects that and returns the tuple)
            ('W15', 'W19', 1, 596.11, 'Sea')
    
        >>> if_disconnected(G, "W24", "W5")
            (There is no such warehouse, i.e., W24 in the dataset, so it returns None)
            None

        >>> if_disconnected(G, "W1", "W11") 
            (Shipment Method between W1 and W11 is via Sea, so if we remove this connection, we look for the next faster 
              Sea shipment from W1, however, there is no other Sea shipment originating from W1, so it returns -1)
            -1
    """

    # WRITE YOUR CODE HERE
    P = is_connected(graph, warehouse_o, warehouse_i)
    if P == False or P == None:
        return P
    Q = False
    for i in graph:
        if i[0] == warehouse_o:
            Q = True
    if Q == False:
        return None
       
    D = list_of_incident_edges(graph,warehouse_o)
    T = []
    for i in D:
        if i[1] == warehouse_i:
            method = i[4]
            D.remove(i)
            for j in D:
                if j[4] == method:
                    T.append(j)
                    break
    if T == []:
        return -1
    cost = 1000
    route = None
    for k in T:
        if k[2] <cost:
            cost = k[2]
            route = k
    w = route[0]
    return(w[0],route[1],route[2],route[3],route[4])

    


    
    


def main():
    G = create_supply_chain('supply_chain.csv')
    f = is_connected(G, "W1", "W11")
    print(f)


    """
    EXPECTED OUTPUT:
    True
    """

    f = is_connected(G, "W1", "W15")
    print(f)

    """
    EXPECTED OUTPUT:
    False
    """
    
    f = is_connected(G, "W1", "W1")
    print(f)
    
    """
    EXPECTED OUTPUT:
    False
    """
    
    f = is_connected(G, "W1", "W24")
    print(f)

    """
    EXPECTED OUTPUT:
    False
    """
    
    f = if_disconnected(G, "W15", "W5")
    print(f)

    """
    EXPECTED OUTPUT:
    ('W15', 'W19', 1, 596.11, 'Sea')
    """

    f = if_disconnected(G, "W24", "W5")
    print(f)

    """
    EXPECTED OUTPUT:
    None
    """

    f = if_disconnected(G, "W1", "W11")
    print(f)

    """
    EXPECTED OUTPUT:
    -1
    """

if __name__ == "__main__":
    main()
