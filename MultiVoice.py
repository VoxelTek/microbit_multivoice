#Imports the nececary libraries
from microbit import *
import music
import utime

freqs = []

notes = []

note_time = 0

time = 0

while True:
    notescheck()
    freqscheck()
    for loop in range(len(freqs):
        music.pitch(freqs[loop][0], 10)


def notescheck():
    if notes[note_time][1] <= time:
        freqs.append(notes[note_time])
        note_time = note_time + 1
        notecheck()


def freqscheck():
    for length in repeat(len(freqs)):
        if freqs[length][2] <= time:
            freqs.del(length)
