#!/usr/bin/python

import json, time, random, copy, thread
import sys
import pypot.robot
from pypot.primitive.move import Move

################
# key pressed detection without interruptig code
# from http://rosettacode.org/wiki/Keyboard_input/Keypress_check#Python
################

try:
    from msvcrt import getch  # try to import Windows version
except ImportError:
    def getch():   # define non-Windows version
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
 
char = None
 
def keypress():
    global char
    #~ char = None
    char = getch()
    

 ################
# robot cofiguration file
# json file where positios will be saved
################

poppy_config_file = 'poppy_custom_config.json'
saved_positions_file = 'saved_walk_positions.json'


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
 
def readSavedPositions():
    savedPositions = None
    try:
        with open(saved_positions_file ) as f:
            savedPositions = Move.load(f)
            savedPositions = savedPositions._positions
    except:
        savedPositions = []
        
    return savedPositions
    
def savePositionsInFile(positions):
    move = Move(0.)
    move._positions = positions
    with open(saved_positions_file, 'w') as f:
        move.save(f)

def setPosition(poppy, position, t):
    for m in poppy.motors:
        if  m.name in  position.keys():
            m.goto_position(position[m.name], t, wait=False)
        
    time.sleep(t)
    
def smartCompliance(poppy, previous_pos):
    print "press any key when done"
    #create a copy of previous position
    new_pos = copy.deepcopy(previous_pos)
    
    #start listenig to key pressed
    thread.start_new_thread(keypress, ())
    
    while True: #while no key pressed
        for m in controlled_motors :
            
            #define load limit
            limit = 20
            if m.model == "MX-64":
                limit = 12
            #if load exceeds limit, push goal positoin toward current position
            if m.present_load > limit or  m.present_load < -limit :
                pos = 0.5*m.present_position + 0.5* new_pos[m.name]
                new_pos[m.name] = pos
                m.goal_position = pos

        
        #check if some key has been pressed
        global char
        if char is not None:
            char = None
            break

        time.sleep(0.1)
        
    return  new_pos
     
######################

poppy = createPoppyCreature()

#We don't use arms and head
controlled_motors =  poppy.legs + poppy.torso

for m in controlled_motors :
    m.compliant = False
    m.goal_position = 0.0
    m.max_torque = 20    
    
time.sleep(1)

#read positions from file, add zero init pos if nothing to be read
all_poses = readSavedPositions()
if len(all_poses) == 0:
    previous_pos = {}
    for m in controlled_motors:
        previous_pos[m.name] = 0.0
setPosition(poppy, previous_pos, 1)

#ask for the name of next position
name = raw_input("position name (or stop): ")
while name != "stop":
    
    new_pos = smartCompliance(poppy, previous_pos)
    time.sleep(1)
    
    keepPos = raw_input("are you happy with pose "+name+"? y/n ")
    if keepPos == "y":
        print "saving position"
        new_pos["name"] = name
        #~ print new_pos
        all_poses.append(new_pos)
        previous_pos = new_pos
    else:
        print "going back"
        setPosition(poppy, previous_pos, 1)
    
    name = raw_input("position name (or stop): ")
    
savePositionsInFile(all_poses)

print "Warning, robot will remove compliance!"
time.sleep(3)

for m in poppy.motors:
    m.compliant = True
    
time.sleep(0.1)