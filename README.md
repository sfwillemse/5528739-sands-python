I model a simple musical moment: two notes (C4 and F4, a perfect fourth) played like a short duet. One starts, the other joins later, then ends—exactly what happens when two keys are pressed at slightly different Times. This makes the signal ops (gating, time shift, mixing) intuitive and audible/visible- see the added plots. 

 What it simulates
- Notes as sinusoids: C4 = 261.63 Hz, F4 = 349.23 Hz.
- Note on/off: a rectangular gate models pressing/releasing a key.
- Delayed entrance: F4 starts 0.35 s after C4.
- Chord by mixing y = xg_c4 =cx_f4 

Why
I simulate a simple musical moment: C4 starts, F4 (a perfect fourth above) joins later, then ends. This maps cleanly to signal ops we learned.

Method (short)
sample_rate 8000 Hz, duration 1.5 s, gate_length 1.0 s
Discrete time with N = round(duration*sample_rate), t in [0, duration)
Sine: x[n] = sin(2π f n / fs); gate w[n] in {0,1}; 
Gated signal: xg = x · w
Mix:  y = xg_c4 + xg_f4

How to run
Option A: Install numpy and matplotlib; run: python run.py and signals.py
OPtion B: Use pyproject.toml


Outputs
- c4_f4_zoom.png (25 ms zoom)
- c4_f4_gated_time.png (both notes gated 0–1.0 s)
- c4_f4_delayed_time.png (C4-only → overlap → F4-only + mix)

