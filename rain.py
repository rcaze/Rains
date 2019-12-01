from pydub import AudioSegment
from numpy import random
import numpy as np

def build_drops(drop_multp, drops):
    """
    Multiply the sounds by the number of time you want to hear the a drop sound
    """
    return drops * drop_multp


def rain_core(durs, dropss):
    """
    Generate rain sound with different length of time and concatenate them
    """
    out = AudioSegment.silent(duration=sum(durs))
    # Pre-compute the drops time position
    pos = random.randint(0, durs[0], len(dropss[0]))
    t0 = durs[0]
    for i, dur in enumerate(durs[1:]):
        pos = np.concatenate((pos,
                              random.randint(t0,
                                             t0+dur,
                                             len(dropss[i+1]))))
        t0 += dur

    # Flatten the dropss
    drops=[]
    for d in dropss:
        drops += d

    # Overlay the drops
    for i, drop in enumerate(drops):
        out = out.overlay(drop, position=pos[i])
    return out


def last():
    pass

if __name__ == "__main__":
    sc = AudioSegment.from_file('samples/C_major_scale.mid.ogg')
    keys = [sc[1000*i:1000*(i+1)] for i in range(8)]

    dropss = [[keys[0]]*100, [], [keys[0]]*100]
    out = rain_core([10000 for i in range(3)], dropss)
    out.export("rains/PluieDeDo.wav", format="wav")

    do_nuanced = [keys[0].apply_gain(i) for i in range(5)]
    random.shuffle(do_nuanced)
    dropss = [do_nuanced*i for i in range(10)]
    out = rain_core([5000 for i in range(10)], dropss)
    out.export("rains/LaPluieArrive.wav", format="wav")

    dropss = [[keys[i]]*50 for i in range(8)]
    out = rain_core([5000 for i in range(8)], dropss)
    out.export("rains/PluieDeGamme.wav", format="wav")

    dropss = [[keys[0]]*60,
              [keys[0], keys[2]]*30,
              [keys[0], keys[2], keys[4]]*20]
    out = rain_core([10000 for i in range(3)], dropss)
    out.export("rains/PluieD'arpège.wav", format="wav")

    """
    We use here different gain for the same Key falling bringing more texture
    do_nuanced = [keys[0].apply_gain(i) for i in range(5)]
    random.shuffle(do_nuanced)
    dropss = [[keys[0]]*100, do_nuanced*20]
    out = rain_core([10000, 10000], dropss)
    """
