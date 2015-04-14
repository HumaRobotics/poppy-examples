# web-user-interfaces
Some useful graphical tools based on a python webserver
Tested with Ubuntu 14.04, python2.7 and firefox
Warning: I have beginner level in web technologies, so code may be strange or inefficient. Remarks welcome.

#How to use
- If you don't run this from the Odroid, connect your Poppy robot to your computer
- Run the webserver: python webserver.py
- Open the URL http://localhost:8888/index.html in your web browser

If your browser offer to open a python file instad of executing it, try to make it executable (chmod +x fileName.py) or check error in your webserver logs.

The saved position in puppet master are saved in the puppet_master/saved_positions.json file. They use the same format than registered moves, with a name field added.
Asking the robot to go to a position will set motors stored in the position non compliant. Saving a position saves all the motors, even non compliant ones.