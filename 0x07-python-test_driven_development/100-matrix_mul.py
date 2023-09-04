#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must have the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must have the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = [[m_b[j][i] for j in range(len(m_b))] for i in range(len(m_b[0]))]

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = sum(a * b for a, b in zip(row, col))
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
