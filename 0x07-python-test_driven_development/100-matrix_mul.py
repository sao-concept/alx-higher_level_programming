#!/usr/bin/python3
"""Defines an matrix_mul function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers/floats)

    Args:
        m_a (list of lists of ints/floats): the first matrix.
        m_b (list of lists of ints/floats): the second matrix.

    Raises:
        TypeError: if either m_a or m_b is not list or list of
        lists is not an integer or a float
                    or not a rectangle
        ValueError: if either m_a or m_b is empty, or can’t be multiplied
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    list1 = len(m_a)
    if list1 == 0:
        raise ValueError("m_a can't be empty")
    list2 = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if list2 is None:
            list2 = len(i)
            if list2 == 0:
                raise ValueError("m_a can't be empty")
        if list2 != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    list3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if list3 is None:
            list3 = len(i)
            if list3 == 0:
                raise ValueError("m_b can't be empty")
        if list3 != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if list2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(list1):
        list0 = []
        for j in range(list3):
            n = 0
            for k in range(list2):
                n += m_a[i][k] * m_b[k][j]
            list0.append(n)
        matrix.append(list0)
    return matrix
