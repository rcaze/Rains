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


def rain(durs, ndrops, drops):
    """
    Generate rain sound with different length of time and concatenate them
    """
    out = AudioSegment.silent(duration=sum(durs))
    for i, dur in enumerate(durs):
        for ndrop in range(ndrops[i]):
            n = random.randint(len(drops))
            drop = drops[n]
            out = out.overlay(drop,
                              position=random.randint(sum(durs[:i]),
                                                      sum(durs[:i+1])))
    return out


def last():
    pass

if __name__ == "__main__":
    durs = [1000 for i in range(20)]
    ndrops = [i*2 for i in range(20)]
    drops = build_drops(0, 3, keyword="Si")
    out = rain(durs, ndrops, drops)
    out.export("Rains/BsComingRain.wav", format="wav")


