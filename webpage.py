import yattag
#------------------------------------------------------------------------------------------------------------------------
import yaml
from yattag import *
import pdb
import os
#------------------------------------------------------------------------------------------------------------------------
class WebPage:

    siteAnnotationDirectories = [];
    annotationsDirectory = ''
    htmlDoc = None
    htmlText = ''

    #--------------------------------------------------------------------------------
    def __init__(self, directory):

        self.directory = directory
        self.siteAnnotationDirectories = os.listdir(directory)

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
    def toHTML(self):

      htmlDoc = Doc()
      htmlDoc.asis('<!DOCTYPE html>')

      with htmlDoc.tag('html', lang="en"):
          with htmlDoc.tag('head'):
              htmlDoc.asis('<meta charset="UTF-8">')
              htmlDoc.asis(self.getStandardIncludes())
              htmlDoc.asis(self.getCSS())
              htmlDoc.asis(self.getJavascript())
          with htmlDoc.tag('body'):
             with htmlDoc.tag("div", id="map_canvas", klass="mapCanvasClass"):
               htmlDoc.text("yo!")

      self.htmlDoc = htmlDoc
      self.htmlText = htmlDoc.getvalue()
      return(self.htmlText)

    #--------------------------------------------------------------------------------


