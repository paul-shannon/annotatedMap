# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------------------------------------
import sys
sys.path.append("..")
from webpage import *
from siteAnnotation import *
#--------------------------------------------------------------------------------------------------------------
def runTests():

    test_constructor()
    test_toHTML()

#--------------------------------------------------------------------------------------------------------------
def test_constructor():

    print("--- test_constructor")
    directory = "../testSites/sewardParkDemo"
    webpage = WebPage(directory)
    assert(webpage.getDirectory() == directory)
    assert(webpage.getSiteAnnotationDirectories() == ['sewardParkGroundZero', 'sewardParkKingfisherPoint'])

#--------------------------------------------------------------------------------------------------------------
def test_toHTML(display=True):

    print("--- test_toHTML")
    directory = "../testSites/sewardParkDemo"
    webpage = WebPage(directory)

    htmlText = webpage.toHTML()
    filename = "sewardParkDemo.html"
    f = open(filename, "w")
    f.write(indent(htmlText))
    f.close()
    if(display):
       os.system("open %s" % filename)

#--------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    runTests()


