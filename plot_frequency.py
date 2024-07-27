import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile

audio_path = "filtered.wav"


sample_rate, audio_time_series = wavfile.read(audio_path)
single_sample_data = audio_time_series[:sample_rate]


def fft_plot(audio, sample_rate):
    N = len(audio)    # Number of samples
    y_freq = fft(audio)
    domain = len(y_freq) // 2
    x_freq = np.linspace(0, sample_rate//2, N//2)
    # Changed from abs(y_freq[:domain]) -> y_freq[:domain]
    plt.plot(x_freq, y_freq[:domain])
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Frequency Amplitude |X(t)|")
    return plt.show()


# Changed from single_sample_data -> audio_time_series
fft_plot(audio_time_series, sample_rate)
