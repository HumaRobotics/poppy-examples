import json, time, math
import pypot.robot
from pypot.primitive.move import Move, MoveRecorder, MovePlayer
from pypot.primitive import LoopPrimitive



#Use primitive to play movement

class NearestNeighboorWalker(LoopPrimitive):

    def __init__(self, robot, move):
        LoopPrimitive.__init__(self, robot, move.framerate)
        self.positions = move.positions()
        self.motors = robot.motors
        self.maxPreviousPos = 10
        self.previousPoses = []


    def setup(self):
        pass
 
 #distance between two positions is considered as the biggest absolute difference 
 #between the angles of one motor
    def positionDistance(self, p1, p2):
        d = 0.
        for m, v in p1.iteritems():
            newd = math.fabs(v - p2[m])
            if newd > d:
                d = newd
        #~ print d
        return d
       
   #compute the distance between the set of previous poses and a set of same size from the recorded positions
    def positionsDistances(self, p):
        d = 0.
        lenprevious  = len(self.previousPoses)
        for i in range(0, lenprevious ):
            d +=self.positionDistance(self.previousPoses[i], p[i])

        d = d/lenprevious
        return d
        
    def findNextPos(self, currentPos):
        #update previous poses
        nextPos = currentPos
        self.previousPoses.append(currentPos)
        if len(self.previousPoses) > self.maxPreviousPos :
            self.previousPoses = self.previousPoses[1:]
        lenprevious = len(self.previousPoses)
            
        index = 0
        d= 360
        
        #from all recorded positions, find the sequence closest to your prvious poses
        for i in range(0, len(self.positions)-lenprevious ):
            positions = self.positions[i:i+lenprevious ]
            newd = self.positionsDistances(positions)
                
            if newd < d:
                d = newd
                index = i+lenprevious
                nextPos = self.positions[index]

        
        print "i chose position ",index," (",d,")"

        
        return nextPos

    def update(self):
        print "------"
        currentPos = {m.name:m.present_position for m in self.motors}
        
        nextPos = self.findNextPos(currentPos)
        
        #set next position
        try:

            for m, v in nextPos.iteritems():
                getattr(self.robot, m).goal_position = v

        except StopIteration:
            self.stop()
 
####################       

#create poppy robot
#~ poppy_config_file = 'poppy_custom_config.json'


try:
    from poppy_humanoid import PoppyHumanoid
    poppy = PoppyHumanoid()
#~ try:
    
    #~ with open(poppy_config_file) as f:
        #~ poppy_config = json.load(f)  
    #~ poppy = pypot.robot.from_config(poppy_config)
    #~ poppy.start_sync()
except Exception,e:
    print "could not create poppy object"
    print e

    
with open('mymove-test.json') as f:
    loaded_move = Move.load(f)

#set initial position
for m in poppy.motors:
    m.compliant = False
    m.goal_position = 0.0
    m.max_torque = 20

#create primitive object
NNW = NearestNeighboorWalker(poppy, loaded_move)

time.sleep(3)

print "start"    
NNW.start()

time.sleep(30)

print "stop" 
NNW.stop()

for m in poppy.motors:
    m.compliant = True
    
time.sleep(1)