#Imports the nececary libraries
from microbit import *
import music

#Initialises the variables and lists.
freqs = []
while True:
    #Detects if the length of the list is too long.
    if len(freqs) > 10:
        while len(freqs) > 10: #If the list is too long, it checks for zeros and removes them
            for numb in range(len(freqs)):
                if freqs[numb] == 0:
                    break
                else:
                    del freqs[-1]



    #Plays the frequencies.
    for length in range(len(freqs)):
        if freqs[length] != 0: #Checks if the current item in freqs is 0. If so, skip.
            music.pitch(freqs[length], 10)



