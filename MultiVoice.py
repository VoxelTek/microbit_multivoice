#Imports the nececary libraries
from microbit import *
import music

#Initialises the variables and lists.
freqs = [] #Stores the currently playing frequencies.

freqlength = 0 #Used as a temp variable for if there are too many voices

notelist = []
notestart = []
noteend = []


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
    
