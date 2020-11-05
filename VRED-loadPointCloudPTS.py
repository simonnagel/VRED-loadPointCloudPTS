'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided “as is” with no warranty of any kind and you use the applications at your own risk.

Scripted by Simon Nagel, supported by Lionel Graf

Runs only in VRED<2021 as this script is written in Python 2.0

Idea of the script
Polyplanes are created with a resolution res (default 500*500 = 250000 vertices)
Each Vertex will be set to the position of a point of the Point Cloud
The Rendering of the Mesh will change to "Type 0", this stands for rendered as point
The Vertex Color will be changed according to the RGB Value of the Point Cloud
A Chunk material will be added to the Point Cloud. You can change the Size of the Point in the Node Editor.

Use the scripts VRED-reducePointsPTS

Paste the Script to VRED
Please change the path in line 34 to your PTS file path
(optional) Change the Resolution of res
Execute Script
In some cases you need to rescale your PointCloud Node in the scenegraph to see a result.


'''

import math, time

start = time.time()

#### Define PTS file path
datei = file("C:/temp/yourfile.pts",'r')

#### Define Tiles resolution NxN
res = 500

####Read data
daten = datei.read() # weil readlines den Zeilenumbruch mitnimmt
datei.close()
liste = daten.split("\n") # das ist der Zeilen umbruch

####Calc number of tiles
cloudPlen = len(liste)-2
nsplit = int(math.floor(cloudPlen/(res*res)))

####Create Point Cloud Material
mat = createMaterial("UPlasticMaterial") 
mat.setName("Pcloud")
#mat.fields().setVec4f("incandescenceColor",1, 1, 1,1)
pChunk = createChunk("PointChunk");
mat.addChunk(pChunk)

####Create Container
group = createNode("Group","PointCloud")

#### initialize ColorList
colorList =[Vec4f(0.0, 0.0,0.0,1.0),Vec4f(0.0, 1.0,0.0,1.0),Vec4f(0.0, 0.0,1.0,1.0),Vec4f(0.0, 0,0.0,1.0)]
del colorList[:]
gamma = 2.2



####Create Tiles and set Vertices position
count = 0
for n in range(0,nsplit):
    part = createPlane(10.0, 10.0, res, res, 1.0,1.0,1.0)
    part.setName("part"+str(n))
    bla = vrFieldAccess(part.fields().getFieldContainer("texCoords7"))
    if part.fields().hasField('types'):
        typ = vrFieldAccess(part.fields().getFieldContainer("types"))
        typ.setMUInt8('types',[0])
    part.setMaterial(mat)
  
    oldPos = part.getPositions()
    
    for i in range(0,len(oldPos)/3):    
        p = i+1+((len(oldPos)/3)*n)
        value = liste[p].split(" ")
        x = float(value[0])*1000
        y = float(value[1])*1000
        z = float(value[2])*1000
        r = float(value[4])/255
        g = float(value[5])/255
        b = float(value[6])/255
        counterX = i*3+0
        counterY = i*3+1
        counterZ = i*3+2
        oldPos[counterX] = x
        oldPos[counterY] = y
        oldPos[counterZ] = z
        colorList.append(Vec4f(r, g ,b ,1.0))
        colorList[i] = Vec4f(pow(r, gamma), pow(g, gamma),pow(b, gamma),1.0)
        count += len(oldPos)/3
    
    part.setPositions(oldPos)
    group.addChild(part) 
    bla.setMVec4f("TexCoords",colorList)
    del colorList[:]






####Clean Materials
removeUnusedMaterials()

end = time.time()
 
print "Point Cloud Import Completed."
print "Import time: "+str((end-start)/60)+" min."
print str(count+res*res)+" points imported out of "+str(cloudPlen)
