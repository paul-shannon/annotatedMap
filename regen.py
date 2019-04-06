from webpage import *

directory = "regionalSwordFernDieOff"
directory = "testSites/bainbridgeIslandSouth"
webpage = WebPage(directory)

htmlText = webpage.toHTML()
filename = "regionalDieOff.html"
filename = "bainbridgeIslandSouth.html"

f = open(filename, "w")
f.write(indent(htmlText))
f.close()
os.system("open %s" % filename)
