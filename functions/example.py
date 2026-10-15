import pandas as pd


def create_example():
    """
    Returns a data frame example.
    """
    data = pd.DataFrame({
        'Product': ['Café', 'Guaraná', 'Pastel'],
        'Price': [6, 5, 7],
        'Quantity': [20, 10, 15]
    })

    return data