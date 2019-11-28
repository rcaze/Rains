from pydub import AudioSegment
from numpy import random
import numpy as np

def metronome(sound, dur, freq, scale):
    """
    Generate a textured beat
    """
    period = 60000/freq #the time length between two beats
    out = AudioSegment.silent(duration = dur)
    pos = 0
    while pos < dur:
        add = random.normal(scale=scale)
        out = out.overlay(sound, position=pos)
        pos += period+add
    return out


def last():
    pass

if __name__ == "__main__":
    beat = AudioSegment.from_file('samples/benboncan__heartbeat.wav')
    beat = beat[400:950]
    dur = 30000 # duration of the beat in ms
    freq = 200 # Frequency of the beat in Hz
    scale = 20 # The scale of the normal distribution
    out = metronome(beat, dur, freq, scale)
    out.export("metronome/beat0.wav", format="wav")
