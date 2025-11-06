import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    """
    Generating a 1D sine wave. 

    Parameters: 
        frequency (float): Frequency in Hz. 
        duration (float): Length of the signal in seconds 
        sample_rate (int): Samples per second 

    Returns: 
        np.ndarray: Array of shape (N,) with values between -1 and 1, where N = round(duration * sample_rate). 
    """

    N = int(round(duration*sample_rate)) #nmr of discrete samples
    t = np.linspace(0, duration, N, endpoint=False) # 0, 1/sample_rate, ... , (N-1)/sample_rate
    return np.sin(2 * np.pi * frequency * t)

def rectangular_window(start_time, end_time, duration, sample_rate):
    """
    Create a rectangular gate (0/1 array) that is 1 for start_time <= t < end_time.

    Parameters: 
        start_time (float): Gate start time in seconds.
        end_time (float): Gate end time in seconds. 
        duration (float): Total signal duration in seconds. 
        sample_rate (int): Samples per second. 

    Returns: 
        np.ndarray: Float array of shape (N,) with values 0.0 or 1.0. 
    """
    N = int(round(duration*sample_rate)) 
    t = np.linspace(0, duration, N, endpoint=False)
    return ((t>=start_time) & (t<end_time)).astype(float)


def gate_signal(x: np.ndarray, start_time: float, end_time: float, duration: float, sample_rate: int) -> np.ndarray:
    """
    Apply a rectangular gate to a signal. 

    Parameters: 
        x (np.ndarray): Input 1D signal of length N. 
        start_time (float): Gate start time in seconds. 
        end_time (float): Gate end time in seconds. 
        duration (float): Total signal duration in seconds. 
        sample_rate (int): Samples per second. 

    Returns: 
    np.ndarray: Gates signal (same shape as x). 
    """
    w = rectangular_window(start_time, end_time, duration, sample_rate)
    return x * w


def mix_signals(*signals):
    """
    Element-wise sum of multiple 1D signals. 

    Parameters: 
        *singals (np.ndarray): One or more 1D arrays, all with the same length. 

    Returns: 
        np.ndarray: The element-wise sum of all input signals. 

    Raises: 
    ValueError: if no signals are given or their lengths differ.
    """
    if len(signals) == 0:
        raise ValueError("Need at least one signal")
    
    n = len(signals[0])
    for s in signals: 
        if len(s) != n: 
            raise ValueError("All signals must have the same length")
        
    total = signals[0].copy()
    for s in signals[1:]:
        total = total + s 
    return total 
    


