import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    N = int(round(duration*sample_rate)) #nmr of discrete samples
    t = np.linspace(0, duration, N, endpoint=False) # 0, 1/sample_rate, ... , (N-1)/sample_rate
    return np.sin(2 * np.pi * frequency * t)

def rectangular_window(start_time, end_time, duration, sample_rate):
    N = int(round(duration*sample_rate)) 
    t = np.linspace(0, duration, N, endpoint=False)
    return ((t>=start_time) & (t<end_time)).astype(float)
    