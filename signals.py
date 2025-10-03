import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    N = int(round(duration*sample_rate))
    t = np.linspace(0, duration, N, endpoint=False)
    return np.sin(2 * np.pi * frequency * t)
