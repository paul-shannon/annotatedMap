# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------------------------------------
import sys
sys.path.append("..")
from siteAnnotation import *
from marker import *
#--------------------------------------------------------------------------------------------------------------
def runTests():

    test_constructor()
    test_toJavascript()
    test_toJavascriptFile()

#--------------------------------------------------------------------------------------------------------------
def test_constructor():

    print("--- test_constructor")
    siteAnno = SiteAnnotation("../testSites/sewardParkDemo/sewardParkGroundZero/site.yaml")
    marker = Marker(siteAnno, 1)

#--------------------------------------------------------------------------------------------------------------
def test_toJavascript():

    print("--- test_toJavascript")
    siteAnno = SiteAnnotation("../testSites/sewardParkDemo/sewardParkGroundZero/site.yaml")
    marker = Marker(siteAnno, 1)
    s = marker.toJavascript()
       # a very crude test
    assert(len(s.split("\n")) > 50)

#--------------------------------------------------------------------------------------------------------------
def test_toJavascriptFile():

    print("--- test_toJavascriptFile")
    siteAnno = SiteAnnotation("../testSites/sewardParkDemo/sewardParkGroundZero/site.yaml")
    marker = Marker(siteAnno, 1)
    marker.toJavascriptFile("marker_1.js")


#--------------------------------------------------------------------------------------------------------------
runTests()


