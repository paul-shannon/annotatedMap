# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------------------------------------------
import sys
sys.path.append("..")
from siteAnnotation import *
#--------------------------------------------------------------------------------------------------------------
def runTests():

    test_constructor()

#--------------------------------------------------------------------------------------------------------------
def test_constructor():

    print("--- test_constructor")
    siteAnno = SiteAnnotation("../testSites/sewardParkDemo/sewardParkGroundZero/site.yaml")
    assert(siteAnno.getTitle() == "Seward Park Ground Zero")

    assert(siteAnno.getLat() == 47.555474)
    assert(siteAnno.getLon() == -122.248945)
    assert(siteAnno.getRadius() == 100)
    assert(siteAnno.getSeverity() == 10)
    assert(siteAnno.getSummaryTextFile() == "overview.html")
    assert(len(siteAnno.getPhotoTabs()) == 2)
    assert(len(siteAnno.getVideoTabs()) == 1)

#--------------------------------------------------------------------------------------------------------------
runTests()


