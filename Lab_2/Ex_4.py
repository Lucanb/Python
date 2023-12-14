import numpy as np


def Song(M_notes, index, initial):
    song = []
    var = initial
    for i in index:
        var = (var + i) % len(M_notes)
        song.append(M_notes[var])
    return song

if __name__ == '__main__':

    M_notes = ["do", "re", "mi", "fa", "sol"]
    index = [1, -3, 4, 2]
    start_position = 2
    res = Song(M_notes, index, start_position)
    print(res)