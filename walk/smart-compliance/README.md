# walk/smart-compliance
This walk is not balanced, hold your robot!

Update the config of your robot in the poppy_custom_config file (mostly controller ports)

Use the smart-compliance.py file to record positions directly on your robot.
This will make the robot not compliant but it will adapt its position if you try to make it move.

Code output should look like:
```bash
python smart-compliance.py 

position name (or stop): mypos1
press any key when done
are you happy with pose mypos1? y/n y
saving position
position name (or stop): mypos2
press any key when done
are you happy with pose mypos2? y/n n
going back
position name (or stop): stop
Warning, robot will remove compliance!
 ```

The positions are stored in a json file.

Then play them in a cycle usig the walk-from-positions.py file to make the robot walk.

