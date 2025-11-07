import numpy as np 
from signals import generate_sine_wave, rectangular_window, gate_signal, mix_signals, _n_samples

def test_n_samples_correct_and_invalid():
    """
   Check normal rounding cases and that invalid inputs raise ValueError
    """
    assert _n_samples(1.0, 8) == 8
    assert _n_samples(0.5, 8) == 4 

    try:
        _n_samples(-0.1, 8) #duration < 0
        assert False, "expected ValueError for duration<0"
    except ValueError:
        pass 


def test_generate_sine_wave_length_and_type():
    """
    Ensures  'generate sine_wave' returns a NumPy array of the requested length and type. 

    """
    x = generate_sine_wave(2.0, duration=1.0, sample_rate=8) # 8 samples 
    assert isinstance(x, np.ndarray)
    assert len(x) == 8


def test_generate_sine_wave_known_values():
    """f=2 Hz, fs=8 samples match [0, 1, 0, -1, ...]"""
    x = generate_sine_wave(2.0, duration=1.0, sample_rate=8)
    expected = np.array([
        0.0, 1.0, 0.0, -1.0, 
        0.0, 1.0, 0.0, -1.0
    ])
    assert np.allclose(x, expected, atol=1e-12)

def test_generate_sine_wave_bounds_and_zero_duration():
    """amplitudes should be whitin [-1, 1]; zero duration returns an empty array."""
    x = generate_sine_wave(5.0, duration=0.2, sample_rate=100)
    assert np.all(x <= 1.0) and np.all(x >=-1.0)

    # duration = 0 -> N = 0 -> emptry array
    x0 = generate_sine_wave(5.0, duration=0.0, sample_rate=100)
    assert isinstance(x0, np.ndarray) and x0.size == 0

def test_rectangular_window_basic():
    """
    Window is ON from 0.225s to 0.50s (start included, end not). On an 8-point grid, 
    that means only indices 2 and 3 are 1.
    """
    w = rectangular_window(0.25, 0.50, duration=1.0, sample_rate=8)
    assert len(w) == 8
    assert list(w[:5]) == [0.0, 0.0, 1.0, 1.0, 0.0]

def test_rectangular_window_boundaries():
    """
    Edge rules: duration -> all ones; zero width -> all zeros; the end time is NOT included. 
    """
    fs = 8 
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
    """
    Adding signals works element-by-element for 2 or 3 inputs.
    """
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([0.5, -1.0, 4.0])
    c = np.array([2.0, 0.0, -2.0])

    two = mix_signals(a, b)
    three = mix_signals(a, b, c)

    assert np.allclose(two, np.array([1.5, 1.0, 7.0]))
    assert np.allclose(three, np.array([3.5, 1.0, 5.0]))

def test_mix_signals_does_not_modify_inputs():
    """
    Mixing should not change the originial arrays.
    """
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([0.5, -1.0, 4.0])
    a_copy = a.copy()
    b_copy = b.copy()

    _ = mix_signals(a, b) 
    #originals should be unchanged
    assert np.allclose(a, a_copy)
    assert np.allclose(b, b_copy)

def test_gate_signal_full_and_empty_window():
    """
    Full window -> same signal back. Zero-width window -> all zero. 
    """
    fs = 8
    x = generate_sine_wave(2.0, duration=1.0, sample_rate= fs)

    #Full-on 
    g_full = gate_signal(x,0.0, 1.0, duration=1.0, sample_rate=fs)
    assert np.allclose(g_full, x)

    #empty 
    g_empty = gate_signal(x, 0.5, 0.5, duration=1.0, sample_rate=fs)
    assert np.allclose(g_empty, np.zeros_like(x))








