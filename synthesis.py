import numpy as np
import IPython
from IPython.display import display, Audio, HTML
import scipy
from scipy import signal
from scipy.signal import spectrogram
from scipy.io import wavfile
from flask import Flask
import random
import matplotlib.pyplot as plt

app = Flask(__name__)


# Make a sound player function that plays array "x" with a sample rate "rate", and labels it with "label"
def sound( x, rate=8000, label=''):
    display( HTML( 
    '<style> table, th, td {border: 0px; }</style> <table><tr><td>' + label + 
    '</td><td>' + Audio( x, rate=rate)._repr_html_()[3:] + '</td></tr></table>'
    ))

# Returns noise samples
def make_noise( duration=1, sample_rate=8000):
    samples = []
    for i in range(sample_rate):
        samples.append(random.randn())
    return samples

@app.route('/')
def hello():
    sound_sr, sound = wavfile.read('80s.wav')
    frequencies, times, spectrogram = signal.spectrogram(sound, sound_sr)

    plt.pcolormesh(times, frequencies, spectrogram)
    plt.imshow(spectrogram)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()
    return "Read file", 200