import numpy as np
import matplotlib.pyplot as plt


from signals import generate_sine_wave 

def main():
    frequency = 5
    duration = 2.0
    sample_rate = 100 

    y = generate_sine_wave(frequency, duration, sample_rate)

    N = int(round(duration * sample_rate))
    t = np.linspace(0, duration, N, endpoint=False)

    plt.figure()
    plt.plot(t,y)
    plt.title(f"{frequency} Hz sine wave")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    



if __name__ == "__main__": 
    main()
    