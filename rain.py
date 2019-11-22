from pydub import AudioSegment
from numpy import random

def rain(dur, ndrops, drop):
    """
    Generate rain sound using a single wav file
    """
    silence = AudioSegment.silent(duration=dur)
    drop_time = random.rand()
    out = silence.overlay(drop, position=drop_time*len(silence))
    for i in range(ndrops):
        drop_time = random.rand()
        out = out.overlay(drop, position=drop_time*len(silence))
    return out

def last():
    """Function for nice folding in vim"""
    pass

if __name__ == "__main__":
    dur = 10000
    ndrops = 300
    drop = AudioSegment.from_wav("/home/rcaze/Documents/Musique/Si0.wav")
    out = rain(dur, ndrops, drop)
    out.export("B-rain.wav", format="wav")
