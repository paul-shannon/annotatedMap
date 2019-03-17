import yattag
#------------------------------------------------------------------------------------------------------------------------
import yaml
from yattag import *
import pdb
import os
import sys
#------------------------------------------------------------------------------------------------------------------------
sys.path.append("..")
from siteAnnotation import *
from marker import *
#------------------------------------------------------------------------------------------------------------------------
class WebPage:

    siteAnnotationDirectories = [];
    annotationsDirectory = ''
    htmlDoc = None
    htmlText = ''
    mapCenterLat = None
    mapCenterLon = None
    mapZoom = None

    #--------------------------------------------------------------------------------
    def __init__(self, directory):

        assert(os.path.isdir(directory))
        self.directory = directory
        configFile = os.path.join(directory, "config.yaml")
        assert(os.path.exists(configFile))
        config = yaml.load(open(configFile))
        keys = list(config.keys())
        assert("mapCenter" in keys)
        assert("mapZoom" in keys)
        self.mapCenterLat = config["mapCenter"]["lat"]
        self.mapCenterLon = config["mapCenter"]["lon"]
        self.mapZoom = config["mapZoom"]
        subDirsAndFiles = os.listdir(directory)
        subDirsAndFilesFullPath = [os.path.join(directory, f) for f in subDirsAndFiles]
        self.siteAnnotationDirectories = [f for f in subDirsAndFilesFullPath if os.path.isdir(f)]

    #--------------------------------------------------------------------------------
    def getDirectory(self):

        return(self.directory)

    #--------------------------------------------------------------------------------
    def getSiteAnnotationDirectories(self):

        return(self.siteAnnotationDirectories)

    #--------------------------------------------------------------------------------
    def getStandardIncludes(self):

       includeText = """
          <link href='http://code.google.com/apis/maps/documentation/javascript/examples/default.css' rel='stylesheet' type='text/css'>
          <script src='https://code.jquery.com/jquery-1.12.4.js'></script>
          <script src='https://code.jquery.com/ui/1.12.1/jquery-ui.js'></script>
          <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/themes/base/jquery-ui.css' type='text/css'>

        """
       googleApiKeyFilename = os.path.join(os.path.split(os.path.abspath(__file__))[0], "googleApi.key")
       assert(os.path.exists(googleApiKeyFilename))
       googleApiScriptStatement =  open(googleApiKeyFilename).read()


       return("%s\%s" % (includeText, googleApiScriptStatement))

    #--------------------------------------------------------------------------------
    def getCSS(self):
       cssFilename = os.path.join(os.path.split(os.path.abspath(__file__))[0], "map.css")
       assert(os.path.exists(cssFilename))
       css = "<style>\n%s</style>" % open(cssFilename).read()
       return(css)

    #--------------------------------------------------------------------------------
    def getJavascript(self):

      jsFilename = os.path.join(os.path.split(os.path.abspath(__file__))[0], "map.js")
      assert(os.path.exists(jsFilename))
      jsSource = "<script>\n%s</script>" % open(jsFilename).read()
      return(jsSource)

    #--------------------------------------------------------------------------------
    def generateMarkerJavascriptFunctions(self):

       markerNumber = 0
       markerFunctionFileNames = []

       for siteAnnotationDirectory in self.siteAnnotationDirectories:
          print("--- creating js function for site descirbed in %s" % siteAnnotationDirectory)
          markerNumber += 1
          yamlFile = os.path.join(siteAnnotationDirectory, "site.yaml")
          assert(os.path.exists(yamlFile))
          siteAnnotation = SiteAnnotation(yamlFile)
          marker = Marker(siteAnnotation, markerNumber)
          filename = "marker_%d.js" % markerNumber
          print(" writing marker function to %s" % filename)
          markerFunctionFileNames.append(filename)
          marker.toJavascriptFile(filename)

       return(markerFunctionFileNames)

    #--------------------------------------------------------------------------------
    def getMarkerJavascriptFunctions(self, markerFunctionFileNames):

      jsSource = "";

      createMarkersFunction = "function createMarkers(){"

      for jsFilename in markerFunctionFileNames:
         jsFilenamePath = os.path.join(os.getcwd(), jsFilename)
         print("wish to load javascript marker function file: %s" % jsFilenamePath)
         assert(os.path.exists(jsFilenamePath))
         jsSource = jsSource + "<script>\n%s</script>" % open(jsFilenamePath).read()
         functionShortName = jsFilename.replace(".js", "")
         createMarkersFunction += " create_%s();" % functionShortName;

      createMarkersFunction += "}\n"
      jsSource = jsSource + "<script>\n%s</script>" % createMarkersFunction

      return(jsSource)

    #--------------------------------------------------------------------------------
    def toHTML(self):

      markerFunctionFileNames = self.generateMarkerJavascriptFunctions()

      htmlDoc = Doc()
      htmlDoc.asis('<!DOCTYPE html>')

      with htmlDoc.tag('html', lang="en"):
          with htmlDoc.tag('head'):
              htmlDoc.asis('<meta charset="UTF-8">')
              htmlDoc.asis(self.getStandardIncludes())
              htmlDoc.asis(self.getCSS())
              htmlDoc.asis(self.getJavascript())
              htmlDoc.asis(self.getMarkerJavascriptFunctions(markerFunctionFileNames))
          with htmlDoc.tag('body'):
             with htmlDoc.tag("div", id="map_canvas", klass="mapCanvasClass"):
               htmlDoc.text("yo!")

      self.htmlDoc = htmlDoc
      self.htmlText = htmlDoc.getvalue()
      return(self.htmlText)

    #--------------------------------------------------------------------------------


