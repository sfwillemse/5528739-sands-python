import numpy as np 
from signals import generate_sine_wave, rectangular_window, gate_signal, mix_signals

def test_generate_sine_wave_length_andtype():
    x = generate_sine_wave(2.0, duration=1.0, sample_rate=8) # 8 samples 
    assert isinstance(x, np.ndarray)
    assert len(x) == 8


def test_ractangular_window_basic():
    # 1 second, 8 Hz -> samples at t = 0.00, 0.125, 0.250, 0.375, ...
    w = rectangular_window(0.25, 0.50, duration=1.0, sample_rate=8)
    #gate should be 1 for t in [0.25, 0.50) -> indues 2 and 3
    assert len(w) == 8
    assert list(w[:5]) == [0.0, 0.0, 1.0, 1.0, 0.0]

