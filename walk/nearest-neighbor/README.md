# walk/nearest-neighbor
This walk is not balanced, hold your robot!

This code was tested with only the legs and pelvis. It should adapt to a whole Poppy Humanoid, but you may wish to change the distance computed in walk-nearest-neighboor.py at line 38.

Use save_moves.py to record your Poppy Humanoid robot while you apply a walking movement to its body (using some smart trick ;) ).

![](img/walk_record.JPG)  

Then use the walk-nearest-neighboor.py to reconstruct a walk movement where Poppy uses as next position the position in the recorded sequence closest to its recent past positions.
As the robot is partly compliant, you will not end up with exactly the recorded move.
