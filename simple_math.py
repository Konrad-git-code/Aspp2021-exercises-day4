"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Addition of two numbers.

    Parameters
    ----------
    a : int, float
        Number to be added.
    b : int, float
        Number to be added.

    Returns
    ----------
    int, float
        The result of the addition.

    """
    return a+b

def simple_sub(a,b):
    """
    Subtraction of two numbers.

    Parameters
    ----------
    a : int, float
        Number to be subtracted.
    b : int, float
        Number to be added.

    Returns
    ----------
    int, float
        The result of the subtraction.

    """
    return a-b

def simple_mult(a,b):
    """
    Multiplication of two numbers.

    Parameters
    ----------
    a : int, float
        Number to be multiplied.
    b : int, float
        Number to be multiplied.

    Returns
    ----------
    int, float
        The result of the multiplication.
    """
    return a*b

def simple_div(a,b):
    """
    Division of two numbers.

    Parameters
    ----------
    a : int, float 
        Number to be divided. 
    b : int, float 
        Number to be divided. 

    Returns
    ----------
    int, float
        The result of the division. 
    """
    return a/b

def poly_first(x, a0, a1):
    """
    First order polynomial

    Parameters
    ----------
    x : int,float
        Variable in the polynomial.
    a0 : int, float
        Coefficient for the constant in the polynomial.
    a1 : int, float
        Coefficient for the first order variable in the polynonmial.

    Returns
    ----------
    int, float
        The first order polynomial evaluated at `x` with the given coefficients.
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Second order polynomial

    Parameters
    ----------
    x : int,float
        Variable in the polynomial.
    a0 : int, float
        Coefficient for the constant in the polynomial. 
    a1 : int, float
        Coefficient for the first order variable in the polynonmial. 
    a2 : int, float
        Coefficient for the second order variable in the polynomial.

    Returns
    -----------
    int, float
        The second order polynomial evaluated at `x` with the given coefficients.
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# ......
