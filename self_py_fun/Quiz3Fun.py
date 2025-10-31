import numpy as np


# This function is merely for BIOS 584 debugging purposes
def compute_D_correct(input_signal):
    r"""
    :param input_signal:
    """
    T_len = len(input_signal)
    signal_diff_one = input_signal[1:] - input_signal[:-1]
    D_val = np.sum(np.sqrt(1+signal_diff_one**2))
    return D_val


