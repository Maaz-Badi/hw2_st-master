import pytest
from Q1 import *
from Q2 import *
from Q3 import *
from Q4 import *
from Q5 import *
from Q6 import *
from Q7 import *
from Q8 import *
from Q9 import *
from Q10 import *
from Q11 import *
from Q12 import *
from Q13 import *


def test_Q1():
    vertices = list_of_vertices('../supply_chain.csv')
    assert vertices == eval("[('W1', 76.14), ('W10', 94.39), ('W11', 70.81), ('W12', 76.02), ('W13', 73.13), ('W14', 93.7), ('W15', 86.31), ('W16', 73.24), ('W17', 82.5), ('W18', 94.33), ('W19', 91.9), ('W2', 78.09), ('W20', 89.33), ('W3', 82.95), ('W4', 73.83), ('W5', 87.41), ('W6', 77.81), ('W7', 86.43), ('W8', 86.2), ('W9', 91.85)]")
    
    edges = list_of_edges('../supply_chain.csv')
    assert edges == eval("[('W1','W11',2,757.96,'Sea'),('W1','W4',11,913.21,'Air'),('W10','W16',1,418.59,'Sea'),('W10','W11',9,556.73,'Sea'),('W11','W1',5,339.96,'Ground'),('W12','W7',9,582.59,'Ground'),('W12','W9',8,485.8,'Sea'),('W12','W2',12,974.87,'Ground'),('W13','W20',6,195.26,'Sea'),('W13','W17',15,284.62,'Ground'),('W13','W6',12,552.92,'Ground'),('W13','W14',11,536.73,'Sea'),('W13','W12',2,661.32,'Sea'),('W14','W1',6,851.19,'Air'),('W14','W10',4,821.98,'Air'),('W14','W17',5,66.43,'Ground'),('W14','W15',1,75.66,'Ground'),('W14','W18',6,738.24,'Sea'),('W14','W12',12,689.56,'Sea'),('W15','W5',3,320.43,'Sea'),('W15','W19',1,596.11,'Sea'),('W15','W10',15,368.41,'Ground'),('W15','W4',2,654.81,'Ground'),('W15','W12',7,509.52,'Sea'),('W16','W10',14,521.95,'Air'),('W16','W11',5,884.69,'Air'),('W16','W2',4,827.64,'Air'),('W16','W7',1,805.83,'Ground'),('W16','W8',11,122.25,'Air'),('W16','W14',15,193.98,'Ground'),('W17','W16',14,923.49,'Air'),('W17','W11',2,255.71,'Ground'),('W17','W18',7,526.41,'Ground'),('W17','W19',6,888.75,'Sea'),('W18','W8',10,836.67,'Ground'),('W18','W14',1,779.06,'Ground'),('W18','W3',11,761.62,'Air'),('W18','W7',2,861.84,'Ground'),('W18','W17',8,896.6,'Sea'),('W18','W13',11,725.71,'Air'),('W19','W17',7,830.31,'Ground'),('W19','W11',7,580.12,'Ground'),('W19','W9',10,82.76,'Ground'),('W19','W13',4,945.58,'Ground'),('W19','W3',6,997.17,'Air'),('W19','W4',14,439.68,'Sea'),('W2','W18',7,765.5,'Sea'),('W2','W19',7,494.7,'Air'),('W2','W5',13,655.03,'Ground'),('W2','W7',13,876.33,'Air'),('W20','W12',13,491.64,'Air'),('W20','W9',8,767.89,'Air'),('W20','W18',7,722.67,'Ground'),('W20','W3',7,373.31,'Ground'),('W20','W5',10,930.21,'Air'),('W20','W17',1,546.54,'Ground'),('W3','W11',4,248.07,'Ground'),('W3','W19',8,488.74,'Ground'),('W4','W17',4,205.89,'Ground'),('W4','W15',15,489.96,'Air'),('W4','W3',15,347.5,'Ground'),('W4','W2',6,944.41,'Ground'),('W5','W4',10,316.61,'Air'),('W5','W13',12,502.91,'Air'),('W5','W1',15,490.32,'Air'),('W5','W2',2,740.04,'Air'),('W6','W4',10,256.43,'Ground'),('W6','W19',2,887.58,'Sea'),('W7','W19',3,642.02,'Sea'),('W7','W8',10,965.04,'Air'),('W7','W11',14,732.91,'Sea'),('W7','W15',14,88.06,'Sea'),('W7','W17',12,749.38,'Ground'),('W8','W12',10,177.52,'Sea'),('W8','W18',13,281.47,'Air'),('W8','W6',14,256.28,'Ground'),('W8','W11',9,262.95,'Air'),('W8','W9',1,619.01,'Ground'),('W9','W16',9,446.04,'Ground'),('W9','W8',2,138.6,'Sea'),('W9','W6',9,738.54,'Ground'),('W9','W12',1,915.7,'Ground'),('W9','W3',12,199.8,'Air'),('W9','W10',4,488.08,'Sea')]")
    
    
def test_Q2():
    G = create_supply_chain('../supply_chain.csv')
    f = get_warehouse_connections(G, "W1", 'o')
    assert f == ['W11', 'W4']
    
    f = get_warehouse_connections(G, "W1", 'i')
    assert f == ['W11', 'W14', 'W5']
    
    f = get_warehouse_connections(G, "W1", 'b')
    assert f == ['W11', 'W4', 'W14', 'W5']
    
    f = get_warehouse_connections(G, "W24", 'o')
    assert f == []
    
    f = get_warehouse_connections(G, "W24", 'i')
    assert f == []
    
    f = get_warehouse_connections(G, "W24", 'b')
    assert f == []
    
    l = get_number_of_warehouse_connections(G, "W1", 'b')
    assert l == 4
    
    l = get_number_of_warehouse_connections(G, "W24", 'b')
    assert l == 0
    
    
def test_Q3():
    G = create_supply_chain('../supply_chain.csv')
    
    f = is_connected(G, "W1", "W11")
    assert f == True
    
    f = is_connected(G, "W1", "W15")
    assert f == False
    
    f = is_connected(G, "W1", "W1")
    assert f == False
    
    f = is_connected(G, "W1", "W24")
    assert f == False
    
    f = if_disconnected(G, "W15", "W5")
    assert f == ('W15', 'W19', 1, 596.11, 'Sea')
    
    f = if_disconnected(G, "W24", "W5")
    assert f is None
    
    f = if_disconnected(G, "W1", "W11")
    assert f == -1
    
    
def test_Q4():
    G = create_supply_chain('../supply_chain.csv')
    
    details = get_supply_route_details(G, "W1", "W11", "time")
    assert details == 2
    
    details = get_supply_route_details(G, "W1", "W11", "cost")
    assert details == 757.96
    
    details = get_supply_route_details(G, "W1", "W11", "mode")
    assert details == "Sea"
    
    details = get_supply_route_details(G, "W1", "W13", "time")
    assert details == -1
    
    details = get_supply_route_details(G, "W34", "W14", "cost")
    assert details is None
    
    
def test_Q5():
    G = create_supply_chain('../supply_chain.csv')
    
    route = get_cheapest_outgoing_supply_route(G, "W14")
    assert route == ('W14', 'W17')
    
    route = get_cheapest_outgoing_supply_route(G, "W24")
    assert route is None
    
    route = get_expensive_outgoing_supply_route(G, "W14")
    assert route == ('W14', 'W1')
    
    route = get_expensive_outgoing_supply_route(G, "W24")
    assert route is None
    
    route = get_cheapest_incoming_supply_route(G, "W14")
    assert route == ('W16', 'W14')
    
    route = get_cheapest_incoming_supply_route(G, "W24")
    assert route is None
    
    route = get_expensive_incoming_supply_route(G, "W14")
    assert route == ('W18', 'W14')
    
    route = get_expensive_incoming_supply_route(G, "W24")
    assert route is None
    
    
def test_Q6():
    import io
    from contextlib import redirect_stdout
    G = create_supply_chain('../supply_chain.csv')
    
    f = io.StringIO()
    with redirect_stdout(f):
        add_supply_link(G, "W1", "W5", (2, 50, "Ground"))
    output = f.getvalue().strip()
    assert output == "Supply link added successfully"
    
    f = io.StringIO()
    with redirect_stdout(f):
        add_supply_link(G, "W1", "W11", (3, 40, "Sea"))
    output = f.getvalue().strip()
    assert output == "Supply link updated successfully"
    
    f = io.StringIO()
    with redirect_stdout(f):
        add_supply_link(G, "W24", "W11", (3, 33.33, "Air"))
    output = f.getvalue().strip()
    assert output == "W24 is not in the supply chain"
    
    
def test_Q7():
    import io
    from contextlib import redirect_stdout
    G = create_supply_chain('../supply_chain.csv')
    
    f = io.StringIO()
    with redirect_stdout(f):
        add_warehouse(G, "W21", 100.0, "W1", (3, 129.96, "Ground"))
    output = f.getvalue().strip()
    assert output == "The warehouse was added successfully"
    
    f = io.StringIO()
    with redirect_stdout(f):
        add_warehouse(G, "W11", 100.00, "W1", (4, 99.96, "Air"))
    output = f.getvalue().strip()
    assert output == "The warehouse already exists"
    
    f = io.StringIO()
    with redirect_stdout(f):
        add_warehouse(G, "W24", 100.00, "W25", (4, 99.96, "Sea"))
    output = f.getvalue().strip()
    assert output == "The destination warehouse does not exist"
    
    
def test_Q8():
    import io
    from contextlib import redirect_stdout
    G = create_supply_chain('../supply_chain.csv')
    
    f = io.StringIO()
    with redirect_stdout(f):
        remove_supply_link(G, "W1", "W11")
    output = f.getvalue().strip()
    assert output == "Supply link removed successfully"
    
    f = io.StringIO()
    with redirect_stdout(f):
        remove_supply_link(G, "W1", "W5")
    output = f.getvalue().strip()
    assert output == "W5 is not linked to W1"
    
    f = io.StringIO()
    with redirect_stdout(f):
        remove_supply_link(G, "W24", "W11")
    output = f.getvalue().strip()
    assert output == "W24 is not in the supply chain"
    
    
def test_Q9():
    import io
    from contextlib import redirect_stdout
    G = create_supply_chain('../supply_chain.csv')
    
    f = io.StringIO()
    with redirect_stdout(f):
        remove_warehouse(G, "W1")
    output = f.getvalue().strip()
    expected_output = """Supply link removed successfully
Supply link removed successfully
Supply link removed successfully
W1 is successfully removed from the supply chain"""
    assert output == expected_output
    
    f = io.StringIO()
    with redirect_stdout(f):
        remove_warehouse(G, "W24")
    output = f.getvalue().strip()
    assert output == "W24 is not in the supply chain"
    
    
def test_Q10():
    G = create_supply_chain('../supply_chain.csv')
    
    result = count_all_supply_chain_connections(G, "W4", "W10")
    assert result == 17345
    
    result = count_all_supply_chain_connections(G, "W1", "W11")
    assert result == 82892
    
    result = count_all_supply_chain_connections(G, "W4", "W4")
    assert result == 0
    
    result = count_all_supply_chain_connections(G, "W24", "W10")
    assert result is None
    
    
def test_Q11():
    G = create_supply_chain('../supply_chain.csv')
    
    assert find_bottlenecks(G, 5, "time") == ['W1', 'W12', 'W13', 'W14', 'W15', 'W16', 'W17', 'W18', 'W19', 'W2', 'W20', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9']
    assert find_bottlenecks(G, 20, "time") == []
    assert find_bottlenecks(G, 330.00, "cost") == ['W1', 'W10', 'W11', 'W12', 'W13', 'W14', 'W15', 'W16', 'W17', 'W18', 'W19', 'W2', 'W20', 'W3', 'W4', 'W5', 'W6', 'W7', 'W9']
    assert find_bottlenecks(G, 1500.00, "cost") == []
    
    
def test_Q12():
    import io
    from contextlib import redirect_stdout
    G = create_supply_chain('../supply_chain.csv')
    
    f = io.StringIO()
    with redirect_stdout(f):
        graph_density(G)
    output = f.getvalue().strip()
    expected_output = "0.22105263157894736\nRelatively Sparse Graph"
    assert output == expected_output
    
    
def test_Q13():
    G = create_supply_chain('../supply_chain.csv')
    
    result = find_best_warehouse(G)
    assert result == ('W10', 94.39)
    
    result = find_worst_warehouse(G)
    assert result == ('W11', 70.81)
    
    