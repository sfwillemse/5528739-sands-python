import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    N = int(round(duration*sample_rate)) #nmr of discrete samples
    t = np.linspace(0, duration, N, endpoint=False) # 0, 1/sample_rate, ... , (N-1)/sample_rate
    return np.sin(2 * np.pi * frequency * t)

def rectangular_window(start_time, end_time, duration, sample_rate):
    N = int(round(duration*sample_rate)) 
    t = np.linspace(0, duration, N, endpoint=False)
    return ((t>=start_time) & (t<end_time)).astype(float)


def gate_signal(x: np.ndarray, start_time: float, end_time: float, duration: float, sample_rate: int) -> np.ndarray:
    w = rectangular_window(start_time, end_time, duration, sample_rate)
    return x * w


def mix_signals(*signals):
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


