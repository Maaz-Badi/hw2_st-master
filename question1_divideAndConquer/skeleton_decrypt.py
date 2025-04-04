import csv
'''
# Decrypt the data using the logic of the Karatsuba algorithm.
# Args:
#   data: List of list consisting of leaves
# Returns:
#   A tuple containing the original two numbers.
'''
def reverse_karatsuba(data, level=0) -> tuple:
    for i in range(len(data)):
        if type(data[i]) == list:
            data[i] = reverse_karatsuba(data[i])

    x = int(str(data[2][0])+str(data[0][0]))
    y = int(str(data[2][1])+str(data[0][1]))
    h = data[2][2]*10
    return (x,y,h)

'''
# This function reads data from a specified file and decrypt data using the logic of the Karatsuba algorithm.
# Args:
#   filename: The name of the file containing input data.
# Returns:
#   A list of tuples, each tuple representing coordinates (x, y).
'''
def main(filename) -> list[tuple[int, int]]:
    with open (filename) as f :
        lines = f . readlines ()
    input = []
    for line in lines :
        input.append(eval(line))
    no_of_input = input.pop(0)
    D = []
    for i in input:
        q = reverse_karatsuba(i, 0)
        D.append((q, q[0] * q[1] * q[2]))
    return D


print(main("input_decrypt.txt"))