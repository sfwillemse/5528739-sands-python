from signals import generate_sine_wave 

def main():
    frequency = 5
    duration = 2.0
    sample_rate = 100 

    y = generate_sine_wave(frequency, duration, sample_rate)
    print(y[:10])

if __name__ == "__main__": 
    main()
    