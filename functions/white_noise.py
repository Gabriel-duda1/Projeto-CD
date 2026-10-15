import numpy as np
import plotly.express as px

def white_noise(
    n = 10,
    var = 10,
    seed = False
):
    """
    Generate white noise.

    args:
        n: number of time points.
        var: The variance
        seed: Seed for reproducible experiments. Default is false.

    """
    time = np.arange(n)
    
    if seed is False:
        values = np.random.randn(n) * var 
    else:
        np.random.seed(seed)
        values = np.random.randn(n) * var
        
    return time, values