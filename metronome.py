from pydub import AudioSegment
from numpy import random
import numpy as np
import pydub

def metronome(sounds, dur, freq, scale):
    """
    Generate a textured beat
    """
    # The pos can be completely outside the loop
    # The duration can have different length
    # Freq could be renamed tempo and scale temp_varition
    # We could add a loudness component also
    # All in all this could be completly merge with the rain.py
    period = 60000/freq #the time length between two beats
    out = AudioSegment.silent(duration = dur)
    pos = 0
    for sound in sounds:
        add = random.normal(scale=scale)
        out = out.overlay(sound, position=pos)
        pos += period+add
    return out


def last():
    pass

if __name__ == "__main__":
    beat = AudioSegment.from_file('samples/benboncan__heartbeat.wav')
    sc = AudioSegment.from_file('samples/C_major_scale.mid.ogg')
    mi = AudioSegment.from_file('samples/pacway__mi-e.m4a')
    sol = AudioSegment.from_file('samples/pacway__sol-g.m4a')
    do = sc[:1000]
    mi = sc[2000:3000]
    sol = sc[4000:5000]
    beat = beat[400:950]
    dur = 6500 # duration of the beat in ms
    freq = 60 # Frequency of the beat in Hz
    #scale = 20 # The scale of the normal distribution
    #out = metronome([beat], dur, freq, scale)
    out0 = metronome([do, mi, sol, mi, do], dur, freq, 0)
    out1 = metronome([do, mi, sol, mi, do], dur, freq, 100)
    out2 = metronome([do, mi, sol, mi, do], dur, freq, 0)
    out3 = metronome([do, mi, sol, mi, do], dur, freq, 100)
    out = out0 + out1 + out2 + out3
    out.export("metronome/Carpegio.wav", format="wav")
