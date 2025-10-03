import numpy as np
import matplotlib.pyplot as plt


from signals import generate_sine_wave, rectangular_window 

def main():
    #Settings
    duration = 1.5
    sample_rate = 8000
    frequency_c4 = 261.63 # C4 in Hz
    frequency_f4 = 349.23 # F4 in Hz (perfect fourth above C4)
    gate_length = 1.0 # seconds each tone is on (starting at t=0) 

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
    
    plt.title("C4 and F4 (time-domain zoom, first 25 ms)")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("c4_f4_zoom.png", dpi=150)


    #figure2 full-duration gated tones 
    delay_f4 = 0.35 #seconds
    window_c4 = rectangular_window(0.0, min(gate_length, duration), duration, sample_rate) 
    window_f4 = rectangular_window(delay_f4, min(delay_f4 +gate_length, duration), duration, sample_rate) 

    #apply gates
    c4_gated = c4 * window_c4
    f4_gated = f4 * window_f4

    mix = c4_gated + f4_gated

    #downsample for readability over time 1.5s 
    plot_step = max(1, sample_rate//200) 
    
    plt.figure(figsize=(10,6))
    plt.plot(t[::plot_step], c4_gated[::plot_step], label=f"C4 0-{gate_length:.2f} s")
    plt.plot(t[::plot_step], f4_gated[::plot_step], label=f"F4 {delay_f4:.2f}-{min(delay_f4 + gate_length, duration):.2f}s", alpha=0.85)

    plt.plot(t[::plot_step], mix[::plot_step], label="mix = C4 + F4", linewidth=2)

    
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title(" C4 only -> overlap -> and F4 only (delayed entrance + mix) ")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("c4_f4_delayed_time.png", dpi=150)

    plt.show()



if __name__ == "__main__": 
    main()
    