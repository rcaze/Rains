from pydub import AudioSegment
from numpy import random

def build_drops(downv, upv, directory= "/home/rcaze/Documents/Musique/",
                keyword = "Enregistrement_"):
    """
    Generate a list of drop sounds from  catalogs of wav files
    """
    drops = []
    for i in range(downv, upv):
        drops.append(AudioSegment.from_wav(directory+keyword+str(i)+".wav"))
    return drops

def rain(durs, ndrops, dropss):
    """
    Generate rain sound with different length of time and concatenate them
    """
    out = AudioSegment.silent(duration=sum(durs))
    for i, dur in enumerate(durs):
        for ndrop in range(ndrops[i]):
            drops = dropss[i]
            n = random.randint(len(drops))
            drop = drops[n]
            out = out.overlay(drop,
                              position=random.randint(sum(durs[:i]),
                                                      sum(durs[:i+1])))
    return out


def last():
    pass

if __name__ == "__main__":
    durs = [5000 for i in range(8)]
    ndrops = [50 for i in range(8)]
    dropss = [build_drops(45+3*i, 45+3*(i+1)) for i in range(8)]
    out = rain(durs, ndrops, dropss)
    out.export("Rains/BsScaleRain.wav", format="wav")
