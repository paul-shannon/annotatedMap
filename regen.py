from webpage import *

directory = "regionalSwordFernDieOff"
webpage = WebPage(directory)

htmlText = webpage.toHTML()
filename = "regionalDieOff.html"
f = open(filename, "w")
f.write(indent(htmlText))
f.close()
os.system("open %s" % filename)
