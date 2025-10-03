import numpy as np
import matplotlib.pyplot as plt


from signals import generate_sine_wave 

def main():
    duration = 1.0
    sample_rate = 8000
    frequency_c4 = 261.63 # C4 in Hz
    frequency_f4 = 349.23 # F4 in Hz (perfect fourth above C4)

    #generate tones 
    c4 = generate_sine_wave(frequency_c4, duration, sample_rate)
    f4 = generate_sine_wave(frequency_f4, duration, sample_rate)

    # Time axis
    N = int(round(duration * sample_rate))
    t = np.linspace(0, duration, N, endpoint=False)

    zoom_end = int(0.025 * sample_rate)
    plt.figure(figsize=(10, 5))
        
    # Plot only the first 25 ms so individual cycles are visible 
    plt.plot(t[:zoom_end], c4[:zoom_end], label=f"C4 {frequency_c4:.2f} Hz")
    plt.plot(t[:zoom_end], f4[:zoom_end], label=f"F4 {frequency_f4:.2f} Hz",alpha=0.85)
    
    plt.title("C4 and F4(time-domain zoom, first 25 ms)")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("c4_f4_zoom.png", dpi=150)
    plt.show()
    



if __name__ == "__main__": 
    main()
    