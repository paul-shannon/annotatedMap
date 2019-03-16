# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------------------------------------
import sys
sys.path.append("..")
from webpage import *
from siteAnnotation import *
from marker import *
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
    testSites = ['sewardParkGroundZero', 'sewardParkKingfisherPoint']
    testSitesFullPaths = [os.path.join(directory, site) for site in testSites]
    assert(webpage.getSiteAnnotationDirectories() == testSitesFullPaths)

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
runTests()


