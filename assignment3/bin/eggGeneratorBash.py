import maya.standalone
maya.standalone.initialize()

#regular commands
import argparse
import maya.cmds as cmds
import math

#setup argeparse so that user can input radius of sphere
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--radius')

#assign argsparse to variable args
args = parser.parse_args()

#define the function that makes a sphere
def createSphere():
    cmds.polySphere(r=args.radius)
    
def eggGenerator():
    obj = cmds.ls(sl=True)
    scalex = float(1)
    scaley = float(1)
    scalez = float(1)
    
    for i in range(1, 34):
        #obj = name of egg geometry
        obj = cmds.duplicate(obj)
        goldenAngle = i * math.radians(137.51)
        cmds.setAttr (obj[0]+'.tx', math.sin(goldenAngle)*math.sqrt(i))
        cmds.setAttr (obj[0]+'.tz', math.cos(goldenAngle)*math.sqrt(i))
        
        #eggs face center
        cmds.setAttr (obj[0]+'.ry', math.degrees(goldenAngle)+180)
        
        #eggs rotate more as radius grows
        cmds.setAttr (obj[0]+'.rx', -1*i)
        
        #eggs get bigger as radius grows
        cmds.setAttr (obj[0]+'.sx', scalex)
        cmds.setAttr (obj[0]+'.sy', scaley)
        cmds.setAttr (obj[0]+'.sz', scalez)
        scalex = scalex + 0.1
        scaley = scaley + 0.04
        scalez = scalez + 0.05

#ask user for sphere radius if not already input
if not args.radius:
    size = input("Enter sphere radius:")

#call createSphere function with given radius
args.radius = int(size)
createSphere()

print(f"Created a sphere with a radius of {args.radius}")

#ask user if they want to "make eggs"
makeEggs = input("Make eggs? y|n ")
if makeEggs == str("y"):
    #call egg generation function
    eggGenerator()
    print("Created 34 eggs.")
elif makeEggs == str("n"):
    print("You silly goose.")
    exit()
else:
    print("I'll take that as a yes.")
    eggGenerator()
    print("Created 34 eggs.")

#ask user for a place to save the file
fileLocation = str(input("Enter directory path to save the maya file. Include the name you'd like to give the file at the end of the path: "))
#rename and save the maya file from bash
cmds.file(rename=fileLocation)
cmds.file(save=True)
