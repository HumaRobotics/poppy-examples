#!/usr/bin/python
import cgi
form = cgi.FieldStorage()                 # parse form data
print('Content-type: text/html\n')        # hdr plus blank line
print('<title>Poppy Humanoid interactive configuration creation</title>')        # html reply page

#TODO : remove all copy-pasting. Read the full poppy-humanoid conf file and create custom file from it.
    
parts = []

possible_parts = ['head', 'torso', 'larm', 'rarm', 'lleg', 'rleg']

for p in possible_parts:
    if p in form:
        parts.append(p)



def lleg(config):
    config["motors"]["l_hip_y"] = {
      "offset": 2.0,
      "type": "MX-64",
      "id": 13,
      "angle_limit": [
        -105,
        85
      ],
      "orientation": "direct"
    }
    
    config["motors"]["l_hip_z"] = {
      "offset": 0,
      "type": "MX-28",
      "id": 12,
      "angle_limit": [
        -40,
        25
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["l_ankle_y"] =  {
      "offset": 0.0,
      "type": "MX-28",
      "id": 15,
      "angle_limit": [
        -35,
        70
      ],
      "orientation": "direct"
    }
    
    config["motors"]["l_knee_y"] = {
      "offset": 0.0,
      "type": "MX-28",
      "id": 14,
      "angle_limit": [
        -2,
        120
      ],
      "orientation": "direct"
    }
    
    config["motors"]["l_hip_x"] = {
      "offset": 0.0,
      "type": "MX-28",
      "id": 11,
      "angle_limit": [
        -22,
        45
      ],
      "orientation": "direct"
    }
    
    poppy_config['motorgroups'] ["l_leg"] = [
      "l_hip_x",
      "l_hip_z",
      "l_leg_sagitall"
    ]
    
    poppy_config['motorgroups'] ["l_leg_sagitall"] = [
      "l_hip_y",
      "l_knee_y",
      "l_ankle_y"
    ]
    


def rleg(config):
    config["motors"]["r_hip_y"] = {
      "offset": 0.0,
      "type": "MX-64",
      "id": 23,
      "angle_limit": [
        -85,
        105
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["r_knee_y"] = {
      "offset": 0.0,
      "type": "MX-28",
      "id": 24,
      "angle_limit": [
        -120,
        2
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["r_ankle_y"] = {
      "offset": 0.0,
      "type": "MX-28",
      "id": 25,
      "angle_limit": [
        -70,
        25
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["r_hip_z"] = {
      "offset": 0,
      "type": "MX-28",
      "id": 22,
      "angle_limit": [
        -25,
        40
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["r_hip_x"] = {
      "offset": 0.0,
      "type": "MX-28",
      "id": 21,
      "angle_limit": [
        -45,
        20
      ],
      "orientation": "direct"
    }
    
    poppy_config['motorgroups'] ["r_leg"] = [
      "r_hip_x",
      "r_hip_z",
      "r_leg_sagitall"
    ]
    
    poppy_config['motorgroups'] ["r_leg_sagitall"] = [
      "r_hip_y",
      "r_knee_y",
      "r_ankle_y"
    ]

def rarm(config):
    config["motors"]["r_arm_z"] = {
      "offset": 0.0,
      "type": "MX-28",
      "id": 53,
      "angle_limit": [
        -90,
        90
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["r_shoulder_x"] ={
      "offset": 90.0,
      "type": "MX-28",
      "id": 52,
      "angle_limit": [
        -110,
        105
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["r_shoulder_y"] = {
      "offset": 90,
      "type": "MX-28",
      "id": 51,
      "angle_limit": [
        -155,
        120
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["r_elbow_y"] = {
      "offset": 0.0,
      "type": "MX-28",
      "id": 54,
      "angle_limit": [
        0,
        147
      ],
      "orientation": "indirect"
    }
    
    poppy_config['motorgroups'] ["r_arm"] =  [
      "r_shoulder_y",
      "r_shoulder_x",
      "r_arm_z",
      "r_elbow_y"
    ]
    
def larm(config):
    
    config["motors"]["l_elbow_y"] ={
      "offset": 0.0,
      "type": "MX-28",
      "id": 44,
      "angle_limit": [
        -140,
        0
      ],
      "orientation": "direct"
    }
    
    config["motors"]["l_arm_z"] = {
      "offset": 0.0,
      "type": "MX-28",
      "id": 43,
      "angle_limit": [
        -90,
        90
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["l_shoulder_x"] = {
      "offset": -90.0,
      "type": "MX-28",
      "id": 42,
      "angle_limit": [
        -105,
        110
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["l_shoulder_y"] = {
      "offset": 90,
      "type": "MX-28",
      "id": 41,
      "angle_limit": [
        -120,
        155
      ],
      "orientation": "direct"
    }
    
    poppy_config['motorgroups'] ["l_arm"]= [
      "l_shoulder_y",
      "l_shoulder_x",
      "l_arm_z",
      "l_elbow_y"
    ]
    
def torso(config):
    
    config["motors"]["abs_x"] = {
      "offset": 0.0,
      "type": "MX-64",
      "id": 32,
      "angle_limit": [
        -45,
        45
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["abs_y"] = {
      "offset": 0.0,
      "type": "MX-64",
      "id": 31,
      "angle_limit": [
        -37,
        16
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["abs_z"] = {
      "offset": 0.0,
      "type": "MX-28",
      "id": 33,
      "angle_limit": [
        -80,
        80
      ],
      "orientation": "direct"
    }
    
    config["motors"]["bust_y"] = {
      "offset": 0.0,
      "type": "MX-28",
      "id": 34,
      "angle_limit": [
        -46,
        23
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["bust_x"] ={
      "offset": 0.0,
      "type": "MX-28",
      "id": 35,
      "angle_limit": [
        -40,
        40
      ],
      "orientation": "indirect"
    }
    
    poppy_config['motorgroups'] ["torso"] = [
      "abs_y",
      "abs_x",
      "abs_z",
      "bust_y",
      "bust_x"
    ]
    
def head(config):
    config["motors"]["head_y"] ={
      "offset": 20.0,
      "type": "AX-12",
      "id": 37,
      "angle_limit": [
        -40,
        8
      ],
      "orientation": "indirect"
    }
    
    config["motors"]["head_z"] ={
      "offset": 0.0,
      "type": "AX-12",
      "id": 36,
      "angle_limit": [
        -100,
        100
      ],
      "orientation": "direct"
    }
    
    
    poppy_config['motorgroups'] ["head"] =[
      "head_z",
      "head_y"
    ]


 

poppy_config={}
poppy_config["motors"] = {}
poppy_config["motorgroups"] = {}
poppy_config["controllers"] = {}

if "head" in parts:
    head(poppy_config)
if "torso" in parts:
    torso(poppy_config)
if "larm" in parts:
    larm(poppy_config)
if "rarm" in parts:
    rarm(poppy_config)
if "lleg" in parts:
    lleg(poppy_config)
if "rleg" in parts:
    rleg(poppy_config)
  
  
if   "larm" in parts or "rarm" in parts or "head" in parts or "torso" in parts:
    
    poppy_config["controllers"]["upper_body_controller"] = {
      "sync_read": True,
      "attached_motors": [],
      "port": "auto"
    }
    
    if "head" in parts :
        poppy_config["controllers"]["upper_body_controller"] ["attached_motors"].append("head")
  
    if "torso" in parts :
        poppy_config["controllers"]["upper_body_controller"] ["attached_motors"].append("torso")
  
    
    if "larm" in parts and "rarm" in parts:
        poppy_config['motorgroups'] ["arms"] = [
          "l_arm",
          "r_arm"
        ]
        poppy_config["controllers"]["upper_body_controller"] ["attached_motors"].append("arms")
    
    else:
        if "larm" in parts:
            poppy_config["controllers"]["upper_body_controller"] ["attached_motors"].append("l_arm")
        if "rarm" in parts:
            poppy_config["controllers"]["upper_body_controller"] ["attached_motors"].append("r_arm")
     

    
if "lleg" in parts and "rleg" in parts:
    poppy_config['motorgroups'] ["legs"] = [
      "l_leg",
      "r_leg"
    ]
    
    poppy_config['controllers']["lower_body_controller"] = {
        "sync_read": True,
        "attached_motors": [
        "legs"
        ],
        "port": "auto"
        }
    
    
else:
    if "lleg" in parts:
        poppy_config['controllers']["lower_body_controller"] = {
        "sync_read": True,
        "attached_motors": [
        "l_leg"
        ],
        "port": "auto"
        }
    
    
    if "rleg" in parts:
        poppy_config['controllers']["lower_body_controller"] = {
        "sync_read": True,
        "attached_motors": [
        "r_leg"
        ],
        "port": "auto"
        }
    

import json
#~ poppy_config['controllers']['lower_body_controller']['port'] = "auto"
with open('poppy_custom_config.json','w') as f:
    json.dump(poppy_config, f, indent=2)


html_file = './default_html.html'

f = open(html_file, 'r')

html_file = f.read()

html_list = html_file.split("TO_REPLACE")


toPrint = '<p> Configuration file done for parts '
for p in parts:
    toPrint = toPrint+p+' '
    
toPrint = toPrint +".</p>"

toPrint += "<p> Find the poppy_custom_config.json file in the webserver directory.</p>"
print(html_list[0]+toPrint+html_list[1])
