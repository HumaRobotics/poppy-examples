#!/usr/bin/python
import cgi

import json, time
import pypot.robot








def createPoppyCreature():
    poppy = None

    try:
        from poppy_humanoid import PoppyHumanoid
        poppy = PoppyHumanoid()
    #~ except Exception,e:
    #~ try:
        #~ poppy_config_file = './puppet_master/poppy_custom_config.json'
        #~ with open(poppy_config_file) as f:
            #~ poppy_config = json.load(f)  
        #~ poppy = pypot.robot.from_config(poppy_config)
        #~ poppy.start_sync()
    except Exception,e:
        print "could not create poppy object"
        print e
        
    return poppy
    
def changeCompliance(poppy, form):
    if "stand" in form.keys():
        for m in poppy.motors:
            m.compliant = False
            m.goal_position=0
        return
    if "compliant" in form.keys():
        for m in poppy.motors:
            m.compliant = True
        return
    for m in poppy.motors:
        if  m.name in form.keys():
            m.compliant = not m.compliant
    
def createButtons(poppy):
    toPrint = ""
    
    img_height = 600
    img_width = img_height *776/1087

    motors_positions = {
    "head_y":[0.20,0.08],
    "head_z":[0.72,0.12],
    "l_shoulder_y":[0.76,0.19],
    "l_shoulder_x":[0.76,0.25],
    "l_arm_z":[0.84,0.31],
    "l_elbow_y":[0.53,0.38],
    "r_shoulder_y":[0.06,0.19],
    "r_shoulder_x":[0.06,0.26],
    "r_arm_z":[0.06,0.32],
    "r_elbow":[0.06,0.39],
    "bust_x":[0.55,0.29],
    "bust_y":[0.36,0.33],
    "abs_z":[0.57,0.37],
    "abs_y":[0.34,0.42],
    "abs_x":[0.58,0.44],
    "r_ankle_y":[0.16,0.89],
    "r_knee_y":[0.16,0.75],
    "r_hip_x":[0.16,0.62],
    "r_hip_y":[0.08,0.52],
    "r_hip_z":[0.08,0.46],
    "l_ankle_y":[0.70,0.88],
    "l_knee_y":[0.71,0.75],
    "l_hip_x":[0.74,0.62],
    "l_hip_y":[0.82,0.53],
    "l_hip_z":[0.83,0.45],
    }

    for m in poppy.motors:
        if m.name in motors_positions:
            toPrint += "<p><input type=submit name=\""+m.name+"\" value=\""+m.name+"\" class=\"motorinput\""
            toPrint  +=" style=\"left: "+str(int(motors_positions[m.name][0]*img_width))+"px; top:"+str(int(motors_positions[m.name][1]*img_height))+"px;\n"
            if m.compliant:
                toPrint  += "color:green;"
            else:
                toPrint  += "color:red;"
            toPrint +="\"></p>"
        
    return toPrint


    
def displayWebpage(toPrint):
    
    print('Content-type: text/html\n')        # hdr plus blank line
    print('<title>Poppy Humanoid puppet master</title>')        # html reply page
    html_file = './puppet_master/puppet_master.html'

    f = open(html_file, 'r')
    html_file = f.read()

    html_list = html_file.split("TO_REPLACE")
    
    print(html_list[0]+toPrint+html_list[1])




#####################3

form = cgi.FieldStorage() 
poppy = createPoppyCreature()

toPrint=""
if poppy is None:
    toPrint += "<p>ERROR, could not create poppy creature. Please check that all your motors are plugged and powered.</p>\n"
else:
    changeCompliance(poppy, form)
    toPrint += createButtons(poppy)
displayWebpage(toPrint)

time.sleep(0.1) #otherwise compliance is not applied