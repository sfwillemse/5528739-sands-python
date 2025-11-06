import numpy as np 
from signals import generate_sine_wave, rectangular_window, gate_signal, mix_signals

def test_generate_sine_wave_length_and_type():
    x = generate_sine_wave(2.0, duration=1.0, sample_rate=8) # 8 samples 
    assert isinstance(x, np.ndarray)
    assert len(x) == 8


def test_generate_sine_wave_known_values():
    #f=2 Hz, fs=8 -> x[n] = sin(2π*n/8) = sin(π*n/2)
    x = generate_sine_wave(2.0, duration=1.0, sample_rate=8)
    expected = np.array([
        0.0, 1.0, 0.0, -1.0, 
        0.0, 1.0, 0.0, -1.0
    ])
    assert np.allclose(x, expected, atol=1e-12)

def test_generate_sine_wave_bounds_and_zero_duration():
    # amplitudes should be whitin [-1, 1]
    x = generate_sine_wave(5.0, duration=0.2, sample_rate=100)
    assert np.all(x <= 1.0) and np.all(x >=-1.0)

    # duration = 0 -> N = 0 -> emptry array
    x0 = generate_sine_wave(5.0, duration=0.0, sample_rate=100)
    assert isinstance(x0, np.ndarray) and x0.size == 0

def test_rectangular_window_basic():
    # 1 second, 8 Hz -> samples at t = 0.00, 0.125, 0.250, 0.375, ...
    w = rectangular_window(0.25, 0.50, duration=1.0, sample_rate=8)
    #gate should be 1 for t in [0.25, 0.50) -> indices 2 and 3
    assert len(w) == 8
    assert list(w[:5]) == [0.0, 0.0, 1.0, 1.0, 0.0]

def test_rectangular_window_boundaries():
    fs = 8 
    #full-on window: start=0 end=duration -> all ones
    w_full = rectangular_window(0.0, 1.0, duration=1.0, sample_rate=fs)
    assert np.allclose(w_full, np.ones(fs))

    #start==end -> all zeros
    w_empty = rectangular_window(0.5, 0.5, duration=1.0, sample_rate=fs)
    assert np.allclose(w_empty, np.zeros(fs))

    #right edge exclusivity: t == end_time must be 0
    w = rectangular_window(0.25, 0.50, duration=1.0, sample_rate=fs)
    # index 4 is t=0.50s -> should be 0 
    assert w[4] == 0.0 and w[3] == 1.0 

def test_mix_signals_sum_three_arrays():
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([0.5, -1.0, 4.0])
    c = np.array([2.0, 0.0, -2.0])

    two = mix_signals(a, b)
    three = mix_signals(a, b, c)

    assert np.allclose(two, np.array([1.5, 1.0, 7.0]))
    assert np.allclose(three, np.array([3.5, 1.0, 5.0]))

def test_mix_signals_does_not_modify_inputs():
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([0.5, -1.0, 4.0])
    a_copy = a.copy()
    b_copy = b.copy()

    _ = mix_signals(a, b) 
    #originals should be unchanged
    assert np.allclose(a, a_copy)
    assert np.allclose(b, b_copy)

def test_gate_signal_full_and_empty_window():
    fs = 8
    x = generate_sine_wave(2.0, duration=1.0, sample_rate= fs)

    #Full-on 
    g_full = gate_signal(x,0.0, 1.0, duration=1.0, sample_rate=fs)
    assert np.allclose(g_full, x)

    #empty 
    g_empty = gate_signal(x, 0.5, 0.5, duration=1.0, sample_rate=fs)
    assert np.allclose(g_empty, np.zeros_like(x))








