#!/usr/bin/python3
def magic_calculation(num1, num2):
    """Match bytecode provided"""
    from magic_calculation_102 import add, sub

    if num1 < num2:
        result = add(num1, num2)
        for i in range(4, 6):
            result = add(result, i)
        return (result)

    else:
        return (sub(num1, num2))
