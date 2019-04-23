GlowScript 2.7 VPython
#create lane
lane = box(pos=vec(11.5,0,-(.167/2+.10915)), size=vec(23,1,.167), color=color.orange)
#initialize ball
bowlingBall = sphere(pos=vec(0,0,0), radius=.10915, mass=7.27, color=color.purple, texture=textures.earth) #mass and radius copied from tjhsst study
#initialize gutters 
gutter1 = box(pos=vec(11.5,.5,-(.167/2+.10915)), size=vec(23,0.23495,0.167), color= color.white) #width found on wiki
gutter2 = box(pos=vec(11.5,-.5,-(.167/2+.10915)), size=vec(23,0.23495,.167), color= color.white)
#set "pin" locations
pin1 = sphere(pos=vec(20,0, 0), radius=.0605) #radius from wikipedia; center of first pin is 60ft from where ball is released
rowDist = .30 * sqrt(3)/2
pin2 = sphere(pos=vec(20+rowDist,.30/2,0), radius=.0605)
pin3 = sphere(pos=vec(20+rowDist,-.30/2,0), radius=.0605)
pin4 = sphere(pos=vec(20+2*rowDist,.30,0), radius=.0605)
pin5 = sphere(pos=vec(20+2*rowDist,0, 0), radius=.0605)
pin6 = sphere(pos=vec(20+2*rowDist,-.30,0), radius=.0605)
pin7 = sphere(pos=vec(20+3*rowDist,3*.30/2,0), radius=.0605)
pin8 = sphere(pos=vec(20+3*rowDist,-.30/2,0), radius=.0605)
pin9 = sphere(pos=vec(20+3*rowDist,.30/2,0), radius=.0605)
pin10 = sphere(pos=vec(20+3*rowDist,-3*.30/2,0), radius=.0605)

def check_pins():
    if ((bowlingBall.pos.x <= (pin1.pos.x + pin1.radius)) and (bowlingBall.pos.x >= (pin1.pos.x - pin1.radius))):
        if ((bowlingBall.pos.y >= pin1.pos.y - bowlingBall.radius) and (bowlingBall.pos.y <= pin1.pos.y + bowlingBall.radius)):
            print("Pin 1 hit!")
    if ((bowlingBall.pos.x <= (pin2.pos.x + pin1.radius)) and (bowlingBall.pos.x >= (pin2.pos.x - pin1.radius))):
        if ((bowlingBall.pos.y >= pin2.pos.y - bowlingBall.radius) and (bowlingBall.pos.y <= pin2.pos.y + bowlingBall.radius)):
            print("Pin 2 hit!")
        if ((bowlingBall.pos.y >= pin3.pos.y - bowlingBall.radius) and (bowlingBall.pos.y <= pin3.pos.y + bowlingBall.radius)):
            print("Pin 3 hit!")
    if ((bowlingBall.pos.x <= (pin4.pos.x + pin1.radius)) and (bowlingBall.pos.x >= (pin4.pos.x - pin1.radius))):        
        if ((bowlingBall.pos.y >= pin4.pos.y - bowlingBall.radius) and (bowlingBall.pos.y <= pin4.pos.y + bowlingBall.radius)):
            print("Pin 4 hit!")
        if ((bowlingBall.pos.y >= pin5.pos.y - bowlingBall.radius) and (bowlingBall.pos.y <= pin5.pos.y + bowlingBall.radius)):
            print("Pin 5 hit!")
            pin = 5
        if ((bowlingBall.pos.y >= pin6.pos.y - bowlingBall.radius) and (bowlingBall.pos.y <= pin6.pos.y + bowlingBall.radius)):
            print("Pin 6 hit!")
    if ((bowlingBall.pos.x <= (pin7.pos.x + pin1.radius)) and (bowlingBall.pos.x >= (pin7.pos.x - pin1.radius))):
        if ((bowlingBall.pos.y >= pin7.pos.y - bowlingBall.radius) and (bowlingBall.pos.y <= pin7.pos.y + bowlingBall.radius)):
            print("Pin 7 hit!")
        if ((bowlingBall.pos.y >= pin8.pos.y - bowlingBall.radius) and (bowlingBall.pos.y <= pin8.pos.y + bowlingBall.radius)):
            print("Pin 8 hit!")
        if ((bowlingBall.pos.y >= pin9.pos.y - bowlingBall.radius) and (bowlingBall.pos.y <= pin9.pos.y + bowlingBall.radius)):
            print("Pin 9 hit!")
        if ((bowlingBall.pos.y >= pin10.pos.y - bowlingBall.radius) and (bowlingBall.pos.y <= pin10.pos.y + bowlingBall.radius)):
            print("Pin 10 hit!")

def check_gutter():
    fallsIntoGutter = False
    if ((bowlingBall.pos.y > .5) or (bowlingBall.pos.y < -.5)):
        print("Gutter ball!")
        fallsIntoGutter = True
    return fallsIntoGutter
    
#Tower of Pisa pattern
def getOilAndCOF():
    #segmented into 37 unit widths
    widSeg = lane.size.y / 37
    #dark blue of pattern
    if ((bowlingBall.pos.x  < (25/3)) and (bowlingBall.pos.y  > - ((37/2-9) * widSeg)) and (bowlingBall.pos.y  < ((37/2-130) * widSeg))):
        lane.color = color.red
        u = .04 #lowest COF is when there is most oil
    else if ((bowlingBall.pos.x  < (22.5/3)) and (bowlingBall.pos.y  > - ((37/2-8) * widSeg)) and (bowlingBall.pos.y  < ((37/2-11) * widSeg))):
        lane.color = color.red
        u = .04 #lowest COF is when there is most oil
    else if ((bowlingBall.pos.x  < (20/3)) and (bowlingBall.pos.y  > - ((37/2-7) * widSeg)) and (bowlingBall.pos.y  < ((37/2-9) * widSeg))):
        lane.color = color.red
        u = .04 #lowest COF is when there is most oil
    else if ((bowlingBall.pos.x  < (15/3)) and (bowlingBall.pos.y  > - ((37/2-6) * widSeg)) and (bowlingBall.pos.y  < ((37/2-7) * widSeg))):
        lane.color = color.red
        u = .04 #lowest COF is when there is most oil
    else if ((bowlingBall.pos.x  < (10/3)) and (bowlingBall.pos.y  > - ((37/2-5) * widSeg)) and (bowlingBall.pos.y  <  ((37/2-5) * widSeg))):
        lane.color = color.red
        u = .04 #lowest COF is when there is most oil
    else if (bowlingBall.pos.x  < (8/3)):
        lane.color = color.red
        u = .04 #lowest COF is when there is most oil
   
   #mid blue of pattern
    else if (bowlingBall.pos.x < (10/3)):
        lane.color = color.orange
        u = .06 #mid COF
    else if ((bowlingBall.pos.x  < (12.5/3)) and (bowlingBall.pos.y  > - ((37/2-5) * widSeg)) and (bowlingBall.pos.y  < ((37/2-5) * widSeg))):
        lane.color = color.orange
        u = .06 #mid COF
    else if ((bowlingBall.pos.x  < (17.5/3)) and (bowlingBall.pos.y  > - ((37/2-6) * widSeg)) and (bowlingBall.pos.y  < ((37/2-6) * widSeg))):
        lane.color = color.orange
        u = .06 #mid COF
    else if ((bowlingBall.pos.x  < (20/3)) and (bowlingBall.pos.y > - ((37/2-7) * widSeg)) and (bowlingBall.pos.y  < ((37/2-7) * widSeg))):
        lane.color = color.orange
        u = .06 #mid COF 
    else if ((bowlingBall.pos.x  < (22.5/3)) and (bowlingBall.pos.y > - ((37/2-8) * widSeg)) and (bowlingBall.pos.y  < ((37/2-8) * widSeg))):
        lane.color = color.orange
        u = .06 #mid COF
    else if ((bowlingBall.pos.x  < (29/3)) and (bowlingBall.pos.y  > - ((37/2-9) * widSeg)) and (bowlingBall.pos.y  < ((37/2-12) * widSeg))):
        lane.color = color.orange
        u = .06 #mid COF
    else if ((bowlingBall.pos.x  < (32/3)) and (bowlingBall.pos.y > - ((37/2-10) * widSeg)) and (bowlingBall.pos.y  < ((37/2-14) * widSeg))):
        lane.color = color.orange
        u = .06 #mid COF
        
    #light blue of pattern
    else:
        lane.color = color.yellow
        u = .08 #higher COF for minimal oil
    
    #after 40 ft there is NO oil
    if (bowlingBall.pos.x > (40/3)):
        lane.color = color.magenta
        u = .12 #highest COF is when there is no oil
        
    return u


attach_trail(bowlingBall)
t = 0
dt = .01
bowlingBall.vel = vec(17,-.3,0)
vCP = bowlingBall.vel
bowlingBall.w = vec(50**.5, 50**.5, 0)
bowlingBall.I = .033
angle = 0   #angle between vCP and vel
b_angle = 0 #axis tilt angle
c_angle = 0 #axis rotation angle
l = bowlingBall.I * bowlingBall.w
_radius = vec(0,0,-bowlingBall.radius)
temp = 0

while ((t < 10) and (bowlingBall.pos.x < 23)):
    rate(100)
    bowlingBall.pos = bowlingBall.pos + bowlingBall.vel * dt

    check_pins()
    oilu = getOilAndCOF()
    if (check_gutter()):
        t = 10 #exits while loop
    FrictionalForce = (oilu * bowlingBall.mass * 9.81)  * vCP * mag(vCP)
    
    torque = cross(_radius, FrictionalForce)
    l = l + torque * dt
    bowlingBall.w = l /  bowlingBall.I
    b_angle = (bowlingBall.w.y) * dt
    c_angle = (bowlingBall.w.z) * dt

    
    temp = mag(bowlingBall.w * bowlingBall.radius)
    
    angle = mag(bowlingBall.vel)**2 + 2*temp*mag(bowlingBall.vel)*cos(b_angle)*sin(c_angle) + (temp*cos(b_angle))**2 
    angle = angle**-1
    angle = angle * (temp * cos(b_angle) * cos(c_angle))
    
    
    
    FrictionalForce = (oilu * bowlingBall.mass * 9.81)  * vCP * mag(vCP)#simplified but similar to true Frictional Force as in lower oilu resultis in lower FrictionaForce
    tanVel = vec(norm(bowlingBall.vel).y, norm(bowlingBall.vel).x, norm(bowlingBall.vel).z)
    vCP = mag(vCP) * (cos(angle)*tanVel - sin(angle)*norm(bowlingBall.vel))    
   
   #slipping (happens first)
    if (abs(mag(bowlingBall.vel) - mag(vCP)) < 0.001):
        print("slipping")
        bowlingBall.vel = bowlingBall.vel -  FrictionalForce * cos(angle) * dt
        
    
    #rolling (happens last)
    else if (vCP.x = 0):
        print("rolling")
        temp1 = vec(0,0, -.10915) 
        bowlingBall.w = bowlingBall.w + torque / bowlingBall.I * dt 
        bowlingBall.vel= bowlingBall.vel + cross(bowlingBall.w, temp1) * dt
        
    
    #rolling and slipping (happens in between slipping and rolling and is the HOOK)
    else:
        print("hooking")
        temp2 = vec(0, 0, -.10915)
         
        bowlingBall.vel = bowlingBall.vel + (vCP - cross(bowlingBall.w, temp2)) * dt  
        print("tanVel:" + tanVel)
        print("mag of vCP:" + mag(vCP))
    
    
    
    t = t + dt
    
print("done")
