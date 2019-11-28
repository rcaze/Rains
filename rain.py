from pydub import AudioSegment
from numpy import random
import numpy as np

def build_drops(drop_multp, drops):
    """
    Multiply the sounds by the number of time you want to hear the a drop sound
    """
    return drops * drop_multp


def rain_core(dur, drops):
    """
    Generate rain sound with different length of time and concatenate them
    """
    out = AudioSegment.silent(duration=dur)
    pos = random.randint(0, dur, len(drops))
    for i, drop in enumerate(drops):
        out = out.overlay(drop, position=pos[i])
    return out


def match_target_amplitude(sound, target_dBFS):
    """
    Normalize a sound to avoid saturation
    """
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)


def last():
    pass

if __name__ == "__main__":
    #drops = [AudioSegment.from_wav('Enregistrement_%i.wav'%i) for i in range(97, 104)]
    #
    gain_r = 5
    drops = [AudioSegment.from_file('samples/La0.wav', channel=i) for i in range(gain_r)]
    drops = build_drops(20, drops)
    out = rain_core(8000, drops)
    out = match_target_amplitude(out, -30)
    out.export("rains/LaPluie.wav", format="wav")
