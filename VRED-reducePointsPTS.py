"""
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided “as is” with no warranty of any kind and you use the applications at your own risk.

Date: 6th June 2019
Scripted by Michael Rackl, supported by Simon Nagel


This script will reduce the amount of Points of a PTS file.
Change the line_step in line 27. A value of 10 meanus, that every 10th line will be kept, so a value of 10 will reduce the amount of points by factor 10.
A new PTS file with the name *_modified.pts will be saved in the same folder.

Paste the Script to VRED
Modify file name in line 28
Choose line_step in line32
Execute Script and Review File
"""



#################################
# user input
#################################
fi_name = 'c:/temp/yourfile.pts'
# new filename for output
fi_name_new = fi_name.replace('.pts', '') + '_modified.pts'
# stepsize
line_step = 10

#################################
# open and read file for input
#################################
fi = open(fi_name, 'r')
lines = fi.readlines()
fi.close()

#################################
# get subset from input
#################################
out = lines[0::line_step]

#################################
# write output subset to file
#################################
fi_new = open(fi_name_new, 'wt')
fi_new.writelines(out)
fi_new.close()
