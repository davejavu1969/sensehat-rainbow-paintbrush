from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.low_light = True
sense.set_imu_config(True, True, True) 
red = (255, 0, 0)
orange = (255,127,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
indigo = (75,0,130)
violet = (148,0,211)

while True:
    orientation = sense.get_orientation_degrees()
    data = ("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

    pos = data.split(',')[0].lstrip('p: ')
    pos = float(pos)
    if pos >=65 and pos <=90:
        sense.clear(red)
    if pos >=40 and pos <=64:
        sense.clear(orange)
    if pos >=14 and pos <=39:
        sense.clear(yellow)
    if pos >=0 and pos <=13 or pos >=360 and pos <= 351:
        sense.clear(green)
    if pos >=326 and pos <=350:
        sense.clear(blue)
    if pos >=300 and pos <=325:
        sense.clear(indigo)
    if pos >=270 and pos <=299:
        sense.clear(violet)
