# VRED-loadPointCloudPTS
## Use the script to import a Point Cloud from a PTS file.


Runs only in VRED<2021 as this script is written in Python 2.0

Use the [Script VRED-reducePointsPTS.py](VRED-reducePointsPTS.py) to reduce the Amount of Points of the PTS. You might want to start with 1000000 in the first place to get a feeling for import times and performance.

Paste the [Script VRED-loadPointCloudPTS.py](VRED-loadPointCloudPTS.py) to VRED
Please change the path in line 32 to your PTS file path
(optional) Change the Resolution of res
Execute Script


Concept of the script
Polyplanes are created with a resolution res (default 500*500 = 250000 vertices)
Each Vertex will be set to the position of a point of the Point Cloud
The Rendering of the Mesh will change to "Type 0", this stands for rendered as point
The Vertex Color will be changed according to the RGB Value of the Point Cloud
A Chunk material will be added to the Point Cloud. You can change the Size of the Point in the Node Editor.



### VRED-loadPointCloudPTS:

![](VRED-loadPointCloudPTS.gif)
