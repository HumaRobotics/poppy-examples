#!/usr/bin/python

import json, time
import pypot.robot
from pypot.primitive.move import Move

poppy_config_file = 'poppy_custom_config.json'
saved_positions_file = 'example-walk-positions.json'


def createPoppyCreature():
    poppy = None

    #~ try:
        #~ from poppy_humanoid import PoppyHumanoid
        #~ poppy = PoppyHumanoid()
    try:
        
        with open(poppy_config_file) as f:
            poppy_config = json.load(f)  
        poppy = pypot.robot.from_config(poppy_config)
        poppy.start_sync()
    except Exception,e:
        print "could not create poppy object"
        print e
        
    return poppy
    
def initPos(poppy):
    controlled_motors =  poppy.legs + poppy.torso
    
    for m in controlled_motors:
        m.compliant = False
        m.goal_position = 0.0
        m.max_torque = 20    
 
def restPos(poppy):
    for m in poppy.motors:
        m.compliant = True

    time.sleep(0.1)
    
def readSavedPositions():
    savedPositions = None
    try:
        with open(saved_positions_file ) as f:
            savedPositions = Move.load(f)
            savedPositions = savedPositions._positions
    except:
        savedPositions = []
        
    return savedPositions
 
 
def setPosition(poppy, position, t):
    for m in poppy.motors:
        if  m.name in  position.keys():
            m.goto_position(position[m.name], t, wait=False)
        
    time.sleep(t)
    
def goToPosition(poppy, savedPosition, posname, time):
    for p in savedPositions:
        if p["name"] == posname:
            setPosition(poppy, p, time)
            return


################

savedPositions = readSavedPositions()

poppy = createPoppyCreature()

initPos(poppy)

#walk initialization
init = ["init", "right1"]
# full step = move right foot then move left foot
positions = ["right2", "both1", "both2", "left1", "left2", "both3", "both4", "right3"]
#walk termination
stop = ["right1", "init"]


numberOfFullStep = 10 
timeForFullStep = 6. #in seconds
timeByMove = timeForFullStep /len(positions)

for p in init:
    goToPosition(poppy, savedPositions, p, timeByMove)

for i in range(0, numberOfFullStep):
    for p in positions:
        goToPosition(poppy, savedPositions, p, timeByMove)

for p in stop:
    goToPosition(poppy, savedPositions, p, timeByMove)

print "Warning, robot will remove compliance!"
time.sleep(3)
restPos(poppy)