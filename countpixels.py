#!/usr/bin/python/

import Image
import sys
import os

filedir = sys.argv[1]
outputfile = sys.argv[2]

files = os.listdir(filedir)
output = open(outputfile, "w")

for file in files:
	green = 0
	im = Image.open(filedir + file)
	strain = file.split("-")[0]
	colors = im.getcolors(im.size[0]*im.size[1])
	for n in range(len(colors)):
		if colors[n][1] == (0,255,0):
			green = colors[n][0]
			break
	output.write("%s\t%i\t%i\n" % (strain,green,green/25))

output.close()	
