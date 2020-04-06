"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, Keyboard


# TIME_STEP = 64
# MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

keyboard = robot.getKeyboard()
keyboard.enable(1000)
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

yawMotor = robot.getMotor('yaw motor')
swayMotor = robot.getMotor('sway motor')
surgeMotor = robot.getMotor('surge motor')
heaveMotor = robot.getMotor('heave motor')
yawMotor.setPosition(float('inf'))
swayMotor.setPosition(float('inf'))
surgeMotor.setPosition(float('inf'))
heaveMotor.setPosition(float('inf'))
yawMotor.setVelocity(0.0)
swayMotor.setVelocity(0.0)
surgeMotor.setVelocity(0.0)
heaveMotor.setVelocity(0.0)

yawVel = 0.0
swayVel = 0.0
surgeVel = 0.0
heaveVel = 0.0

print '"UP" turns up Yaw'
print '"DOWN" turns down Yaw'
print '"LEFT" turns up Sway'
print '"RIGHT" turns down Yaw'
print '"A" turns up Surge'
print '"D" turns down Surge'
print '"W" turns up Heave'
print '"S" turns down Heave'

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    yawMotor.setVelocity(yawVel)
    swayMotor.setVelocity(swayVel)
    surgeMotor.setVelocity(surgeVel)
    heaveMotor.setVelocity(heaveVel)
    key = keyboard.getKey()
    if (key==Keyboard.UP):
      print 'Yaw + 0.05. Total Yaw velocity:' + str(yawVel)
      yawVel += 0.5
    if (key==Keyboard.DOWN):
      print 'Yaw - 0.05. Total Yaw velocity:' + str(yawVel)
      yawVel -= 0.5
    if (key==Keyboard.LEFT):
      print 'Sway + 0.05. Total Sway velocity:' + str(swayVel)
      swayVel += 0.5
    if (key==Keyboard.RIGHT):
      print 'Sway - 0.05. Total Sway velocity:' + srt(swayVel)
      swayVel -= 0.5
    if (key==ord('A')):
      print 'Surge + 0.05. Total Surge velocity:' + str(surgeVel)
      surgeVel += 0.5
    if (key==ord('D')):
      print 'Surge - 0.05. Total Surge velocity:' + str(surgeVel)
      surgeVel -= 0.5
    if (key==ord('W')):
      print 'Heave + 0.05. Total Heave velocity:' + str(heaveVel)
      heaveVel += 0.5
    if (key==ord('S')):
      print 'Heave - 0.05. Total Heave velocity:' + str(heaveVel)
      heaveVel -= 0.5
       
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    # pass

# Enter here exit cleanup code.
