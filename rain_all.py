from pydub import AudioSegment
from numpy import random

def build_drops(downv, upv, directory= "samples/",
                keyword = "Enregistrement_"):
    """
    Generate a list of drop sounds from  catalogs of wav files
    """
    drops = []
    for i in range(downv, upv):
        drops.append(AudioSegment.from_wav(directory+keyword+str(i)+".wav"))
    return drops


def rain_core(dur, ndrops, drop):
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


def rain_times(durs, ndrops, drop):
    """
    Generate rain sound with different length of time and concatenate them
    """
    out = AudioSegment.silent(duration=sum(durs))
    for i, dur in enumerate(durs):
        for ndrop in range(ndrops[i]):
            out = out.overlay(drop,
                              position=random.randint(sum(durs[:i]),
                                                      sum(durs[:i+1])))
    return out


def rain_times_last(durs, ndrops, drops):
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


def rain_times_scale(durs, ndrops, dropss):
    """
    Generate rain sound with different length of time and concatenate them
    should be able to do all the things the prvious function did
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
    dur = 4000
    ndrops = 600
    drop = AudioSegment.from_wav("samples/Si0.wav")
    out = rain_core(dur, ndrops, drop)
    out.export("rains/B-rain.wav", format="wav")

    durs = [1000 for i in range(20)]
    ndrops = [i*2 for i in range(20)]
    out = rain_times(durs, ndrops, drop)
    out.export("rains/BcomingRain.wav", format="wav")

    durs = [1000 for i in range(20)]
    ndrops = [i*2 for i in range(20)]
    drops = build_drops(0, 3, keyword="Si")
    out = rain_times_last(durs, ndrops, drops)
    out.export("rains/BsComingRain.wav", format="wav")

    durs = [5000 for i in range(8)]
    ndrops = [50 for i in range(8)]
    dropss = [build_drops(45+3*i, 45+3*(i+1)) for i in range(8)]
    out = rain_times_scale(durs, ndrops, dropss)
    out.export("rains/BsScaleRain.wav", format="wav")
