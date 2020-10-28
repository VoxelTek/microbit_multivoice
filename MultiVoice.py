#Imports the nececary libraries
from microbit import *
import music

#Initialises the variables and lists.
freqs = [] #Stores the currently playing frequencies.

freqlength = 0 #Used as a temp variable for if there are too many voices.

time = 0 #Stores the current time in milliseconds.

current-note = 0 #Stores the note that the program is currently at.

temp-loc = 0 #Temporary variable for storing the current position the program is at.
temp-pos = 0

notelist = [] #List of the notes that will be played.
notestart = [] #Records when the notes start.
noteend = [] #Records when the notes end.


notewait = [] #Remembers what notes are currently playing.
notewait-loc = [] #Remembers the position of the currently playing notes in "freqs".


while True:
    notecheck()
    #Plays the frequencies.
    for length in range(len(freqs)): # Repeats for all items in the list.
        if freqlength > 9: #Checks to see if the list has too many notes in it.
            freqlength = 0 #Sets the freqlength variable back to 0.
            length = len(freqs) #Starts the for loop over again, from the beginning.
        else:
            if freqs[length] != 0: #Checks if the current item in freqs is 0. If so, skip.
                freqlength = freqlength + 1
                music.pitch(freqs[length], 10) #Plays a normal note, from the current pitch selected from the "freqs" list.


def notecheck():
    for notelength in range(len(notewait)):
        if noteend(notewait) == time or noteend(notewait) > time:
            del freqs[notewait-loc[notelength]]
            del notewait-loc[notelength]
            del notewait[notelength]
    for loop in range(len(notelist) - current-note):
        temp-loc = - + loop
        temp-pos = -1
        for frequencylength in range(len(freqs)):
            if freqs[frequencylength] == 0:
                temp-pos = frequencylength
        insert(temp-pos)
