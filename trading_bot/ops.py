import os
import math
import logging

import numpy as np


def sigmoid(x):
    """Performs sigmoid operation
    """
    try:
        if x < 0:
            return 1 - 1 / (1 + math.exp(x))
        return 1 / (1 + math.exp(-x))
    except Exception as err:
        print("Error in sigmoid: " + err)

def min_max_normalize(data):
    min_val = np.min(data)
    max_val = np.max(data)
    return (data - min_val) / (max_val - min_val)

def get_state(data, insider_data, t, n_days):
    """Returns an n-day state representation ending at time t
    """

    d = t - n_days + 1
    block = data[d: t + 1] if d >= 0 else -d * [data[0]] + data[0: t + 1]  # pad with t0
    res = []
    for i in range(n_days - 1):
        res.append(sigmoid(block[i + 1] - block[i]))
    
    d = t - n_days + 1
    # Add insider trading features
    insider_res = []
    insider_block = insider_data[d: t + 1] if d >= 0 else -d * [insider_data[0]] + insider_data[0: t + 1]
    for i in range(n_days - 1):
        insider_res.append(sigmoid(insider_block[i + 1] - insider_block[i]))

    final = np.array([res, insider_res])
    return final
