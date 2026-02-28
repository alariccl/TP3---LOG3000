"""
Additionne deux nombres.

Args:
    a (float): Le premier opérande.
    b (float): Le deuxième opérande.

Returns:
    float: La somme de a et b.
"""
def add(a,b):
    return a + b

"""
Soustrait deux nombres.

Args:
    a (float): Le premier opérande (minuende).
    b (float): Le deuxième opérande (subtrahende).

Returns:
    float: Le résultat de la soustraction (a - b).
"""
def subtract(a,b):
    return b - a

"""
Multiplie deux nombres.

Args:
    a (float): Le premier opérande.
    b (float): Le deuxième opérande.

Returns:
    float: Le produit de a et b.
"""
def multiply(a,b):
    return a * b

"""
Divise deux nombres (division entière).

Args:
    a (float): Le dividende.
    b (float): Le diviseur.

Returns:
    float: Le quotient entier de la division (a // b).

Note:
    Lève une exception ZeroDivisionError si b est égal à 0.
"""
def divide(a,b):
    return a / b
