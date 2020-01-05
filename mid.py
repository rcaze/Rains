import mido    # importe bibliothèque Mido
from mido import Message, MidiFile, MidiTrack  # importe modules depuis Mido
import numpy.random as rd
import numpy as np

def build_copinard(delta=68):
    note = [2, 7,
            11, 9, 7, 11,
            9, 7,
            4, 2,
            2, 7,
            11, 9, 7, 11,
            9, 11, 14,
            11, 14, 14,
            11, 9, 7, 11,
            9, 7,
            4, 2,
            2, 7,
            11, 9, 7, 11,
            9, 7]
    note = np.array(note) + delta
    dur  = [1, 2,
            1/3,1/3,1/3, 2,
            1, 2,
            1, 2,
            1, 2,
            1/3,1/3,1/3, 2,
            1,.25, 1.75,
            1.5,.75,.75,
            1/3,1/3,1/3, 2,
            1, 2,
            1, 2,
            1, 2,
            1/3,1/3,1/3, 2,
            1, 3]
    return note, dur


# La partition convertie en valeurs numériques, noctn = notes et noctd = durée notes
notes, dur =  build_copinard()

def trk_b(notes, dur, tempo=700):
    """
    Build a track from a partition
    """
    t_on = 0 # By default the track starts at zero
    for i, note in enumerate(notes):  # boucle notes à jouer dans noctn (notes partition)
        # Randomize
        velp = 20
        vel_on = rd.randint(100-velp, 100+velp)
        vel_off = rd.randint(67-velp, 67+velp)
        jit_f_on = 200
        jit_f_off = 200
        t_on = rd.randint(0, jit_f_on)
        t_off = rd.randint(-jit_f_off, jit_f_off)
        # Adding to the track
        track.append(Message('note_on', channel=1, note = note,
                             velocity = vel_on,
                             time = t_on))
        track.append(Message('note_off', channel=1, note = note,
                             velocity = vel_off,
                             time = int((tempo + t_off) * dur[i])))

    track.append(Message('note_on', channel=1, velocity = 0, time = 32))  # touche final
    track.append(Message('note_off', channel=1, velocity = 0, time = 1024))
    return track


def trk_reg_b(notes, dur, jit_t_off=0.1, temp=700):
    """
    Build a track from a partition
    """
    t_on = 0 # By default the track starts at zero
    for i, note in enumerate(notes):  # boucle notes à jouer dans noctn (notes partition)
        # Randomize
        velp = 20
        vel_on = rd.randint(100-velp, 100+velp)
        vel_off = rd.randint(67-velp, 67+velp)
        t_off_shift = rd.randint(-int(jit_t_off*temp), 0)
        t_off = int(dur[i]*(temp + t_off_shift))
        # Adding to the track
        track.append(Message('note_on', channel=1, note = note,
                             velocity = vel_on,
                             time = t_on))
        track.append(Message('note_off', channel=1, note = note,
                             velocity = vel_off,
                             time = t_off))
        t_on = -t_off_shift

    track.append(Message('note_on', channel=1, velocity = 0, time = 32))  # touche final
    track.append(Message('note_off', channel=1, velocity = 0, time = 1024))
    return track
mid = MidiFile()          # Nous pouvons créer un nouveau fichier en appelant MidiFile
track = MidiTrack()       # sans l’argument du nom de fichier. Le fichier peut ensuite
mid.tracks.append(track)  # être enregistré à la fin en appelant la méthode save()
track = trk_reg_b(notes, dur)
track = trk_b(notes, dur)
mid.save('Hymne_reg.mid')  # enregistre le tout dans ce fichier Midi

