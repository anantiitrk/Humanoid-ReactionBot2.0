#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from subprocess import Popen
k=random.randint(1,3)
print(k)
def playmusic(finalemotion) :
    if finalemotion=="happiness" :
        movie_path = '/home/pi/Desktop/ReactionBot2.0/Songs/happiness/1.mp3'
        omxp = Popen(['omxplayer',movie_path])
      
    elif finalemotion=="sadness"  :
        movie_path = '/home/pi/Desktop/ReactionBot2.0/Songs/sadness/1.mp3'
        omxp = Popen(['omxplayer',movie_path])
        
    else :    
	    movie_path = '/home/pi/Desktop/ReactionBot2.0/Songs/1.mp3'
	    omxp = Popen(['omxplayer',movie_path])
    return
