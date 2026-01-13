"""
EX03 (Tuplas)
Devolver el mínimo y el máximo de una lista.
"""

def min_max_prices(prices: list[float]) -> tuple[float, float]:
    """
    Devuelve una tupla (mínimo, máximo).

    - Si prices está vacía, lanza ValueError.
    """
    if not prices:
        raise ValueError("La lista de precios está vacía")

    minimum = prices[0]
    maximum = prices[0]

    for price in prices[1:]:
        if price < minimum:
            minimum = price
        if price > maximum:
            maximum = price

    return minimum, maximum
