import json, time
import pypot.robot
from pypot.primitive.move import Move, MoveRecorder, MovePlayer


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
    m.max_torque = 20

with open('mymove.json') as f:
    loaded_move = Move.load(f)

player = MovePlayer(poppy, loaded_move)
print "starting"
player.start()
player.wait_to_stop()
print "finished"


for m in poppy.motors:
    m.compliant = True
    print m.name
    
time.wait(1)
