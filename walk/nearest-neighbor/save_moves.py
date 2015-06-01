import json, time
import pypot.robot

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


for m in poppy.motors:
    m.compliant = False
    m.goal_position = 0.0
  
time.sleep(3)    
for m in poppy.motors:
    m.compliant = True
    
from pypot.primitive.move import Move, MoveRecorder, MovePlayer


record_frequency = 20.0 # This means that a new position will be recorded 50 times per second.
recorded_motors = poppy.motors # We will record the position of the 3 last motors of the Ergo

# You can also use alias for the recorded_motors
# e.g. recorder = MoveRecorder(poppy, record_frequency, poppy.tip)
# or even to record all motors position
# recorder = MoveRecorder(poppy, record_frequency, poppy.motors)

recorder = MoveRecorder(poppy, record_frequency, recorded_motors)

for m in recorded_motors:
    m.compliant = True
  
print "start recording"    
recorder.start()

time.sleep(20)

print "stop recording" 
recorder.stop()

recorded_move = recorder.move

with open('mymove.json', 'w') as f:
    recorded_move.save(f)

