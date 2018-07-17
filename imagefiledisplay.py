import cv2
import numpy as np
import time
import serial
from numpy import *
from numpy.random import rand
from time import sleep

random.seed()
ser = serial.Serial('COM4', 9600, timeout=5)
print(ser.name)


#create windows for stimulus presentation
cv2.namedWindow("RTStimulus", cv2.WINDOW_NORMAL)
cv2.namedWindow("RBStimulus", cv2.WINDOW_NORMAL)
cv2.namedWindow("LTStimulus", cv2.WINDOW_NORMAL)
cv2.namedWindow("LBStimulus", cv2.WINDOW_NORMAL)
cv2.resizeWindow("RTStimulus", 5, 5)
cv2.resizeWindow("RBStimulus", 5, 5)
cv2.resizeWindow("LTStimulus", 5, 5)
cv2.resizeWindow("LBStimulus", 5, 5)

datafile=open("datafile.txt", "w")


#let's see about showing an image in a file

stimulusused = [0,0,0,0,0,0,0,0,0,0]
counttrials = 0

  
while counttrials<10:
    
    choice = 0
    counttrials=counttrials + 1

    #Inter-trial interval
    stimulusfile='stimuli/iti.jpg'
    img = cv2.imread(stimulusfile)
    cv2.imshow('LBStimulus', img)
    cv2.imshow('LTStimulus', img)
    cv2.imshow('RBStimulus', img)
    cv2.imshow('RTStimulus', img)
    cv2.waitKey(5)
    #time.sleep(5)

    
    #randomly choose the same stimulus from among the palette of stimuli
    stimulussame = random.randint(0,9)
    stimulusused [stimulussame]=stimulusused [stimulussame] + 1

    #be sure stimuli are different from each other
    x=0
    while x==0:
        stimulusdifft = random.randint(0,9)
        if stimulusdifft <> stimulussame:
            stimulusused [stimulusdifft]=stimulusused [stimulusdifft] + 1
            x=1
    x=0
    while x==0:
        stimulusdiffb = random.randint(0,9)
        if (stimulusdiffb <> stimulussame) and(stimulusdiffb <> stimulusdifft) :
            stimulusused [stimulusdiffb]=stimulusused [stimulusdiffb] + 1
            x=1   
        
    #random does not work right with range of 1,2 (flipping coin) so I use 1, 10 then translate below
    sameside = random.randint(1,10)
    print sameside
    
 #Same stimuli on left
    if sameside < 6:
        sameside = 1
        stimulusfile='stimuli/' + str(stimulussame) + '.jpg'
        img = cv2.imread(stimulusfile)
        cv2.imshow('LTStimulus', img)
        cv2.imshow('LBStimulus', img)

        stimulusfile='stimuli/' + str(stimulusdifft) + '.jpg'
        img = cv2.imread(stimulusfile)
        cv2.imshow('RTStimulus', img)

        stimulusfile='stimuli/' + str(stimulusdiffb) + '.jpg'
        img = cv2.imread(stimulusfile)
        cv2.imshow('RBStimulus', img)

  #Same stimuli on right       
    else:
        sameside = 2
        stimulusfile='stimuli/' + str(stimulussame) + '.jpg'
        img = cv2.imread(stimulusfile)
        cv2.imshow('RTStimulus', img)
        cv2.imshow('RBStimulus', img)

        stimulusfile='stimuli/' + str(stimulusdifft) + '.jpg'
        img = cv2.imread(stimulusfile)
        cv2.imshow('LTStimulus', img)

        stimulusfile='stimuli/' + str(stimulusdiffb) + '.jpg'
        img = cv2.imread(stimulusfile)
        cv2.imshow('LBStimulus', img)

    
    print "trial: ",counttrials, "stimuli: ",stimulussame, stimulusdifft, stimulusdiffb, "Stim count: ", stimulusused [stimulussame], stimulusused [stimulusdifft],stimulusused [stimulusdiffb]
    datafile.write ("counttrials")
 
    
    while choice==0:
        if cv2.waitKey(10)&0xFF==ord('g'):
            choice = 1
        if cv2.waitKey(10)&0xFF==ord('h'):
            choice = 2  
        if cv2.waitKey(10)&0xFF==ord('q'):
            break

    print sameside
    

    ser.write(str(chr(sameside))) # Convert the decimal number to ASCII then send it to the Arduino
    print ser.readline() # Read the newest output from the Arduino
    sleep(.1) # Delay for one tenth of a second
    

        
datafile.close()    
cv2.destroyAllWindows() 
