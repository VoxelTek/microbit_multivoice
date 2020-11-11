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


notewait-time = [] #Remembers what notes are currently playing.
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
                time = time + 10


def notecheck():
    endadd = False
    for length in range(len(notewait-time)):
        if notewait-time[length] == time or if notewait-time[length] < time:
            if notewait-time != -1:
                    freqs[notewait-loc[length]] = 0
                    notewait-loc[length] = -1
                    notewait-time[length] = -1

    if notestart[current_note] <= time:
        for length in range(len(freqs)):
            if freqs[length] == 0:
                endadd = True
                freqs.insert(length, notelist[current_note])
                for i in range(len(notewait-time)):
                    if notewait-time[i] == -1:
                        notewait-time.insert(i, noteend[current_note])
                        notewait-loc.insert(i, length)
                    else:
                        notewait-time.append(noteend[current_note])
                        notewait-loc.append(length)
                
