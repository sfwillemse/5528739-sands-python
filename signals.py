import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(44100 * sample_rate))
    return np.sine(2 * np.pi * frequency * t)
