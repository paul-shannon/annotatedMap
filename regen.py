import sys
from webpage import *

if(len(sys.argv) != 3):
    print("usage: python regen.py <mapDirectory> <mapOut.html>")
    sys.exit(1)

mapDirectory = sys.argv[1]
outputHtmlFile = sys.argv[2]


webpage = WebPage(mapDirectory)

htmlText = webpage.toHTML()

f = open(outputHtmlFile, "w")
f.write(indent(htmlText))
f.close()
os.system("open %s" % outputHtmlFile)
