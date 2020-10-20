#Imports the nececary libraries
from microbit import *
import music

#Initialises the variables and lists.
freqs = []
freqlength = 0

# ----------------NEED TO REDO----------------
#while True: #Detects if the length of the list is too long.
#    if len(freqs) > 10:
#        while len(freqs) > 10: #If the list is too long, it checks for zeros and removes them.
#            for numb in range(len(freqs)):
#                if freqs[numb] == 0:
#                    break
#                else:
#                    del freqs[-1]
# ----------------NEED TO REDO----------------



while True:
    #Plays the frequencies.
    for length in range(len(freqs)): # Repeats for all items in the list.
        freqlength = 0
        if freqlength > 9: #Checks to see if the list has too many notes in it.
            length = len(freqs)
        else:
            if freqs[length] != 0: #Checks if the current item in freqs is 0. If so, skip.
                freqlength = freqlength + 1
                if freqs[length] != -1: # Checks if the current note is a rest or not.
                    music.pitch(freqs[length], 10) #Plays a normal note, from the current pitch selected from the "freqs" list.
                else:
                    music.pitch(0, 10) #Plays an empty note, aka a rest.
