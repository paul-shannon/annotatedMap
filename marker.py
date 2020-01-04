# generate the following javascript function, with embedded HTML, from a SiteAnnotation object
#------------------------------------------------------------------------------------------------------------------------
from yattag import *
import pdb
import os
#------------------------------------------------------------------------------------------------------------------------
class Marker:

    siteAnnotation = None
    markerNumber = None

    def __init__(self, siteAnnotation, markerNumber):
       self.siteAnnotation = siteAnnotation
       self.markerNumber = markerNumber

    #------------------------------------------------------------------------------------------------------------------------
    def toJavascript(self):

        #print("marker.toJavascript, shape: %s" % self.siteAnnotation.shape)
        shape = self.siteAnnotation.shape
        assert(shape in ["circle", "rectangle"]);
        s0 = "";
        if(shape=="circle"):
              s0 = """ function create_marker_%d() {
                var markerLat = %f;
                var markerLon = %f;
                var markerCenter = new google.maps.LatLng(markerLat, markerLon);
                marker = new google.maps.Circle({
                           strokeColor: '%s',
                           strokeOpacity: 0.8,
                           strokeWeight: 2,
                           fillColor: '%s',
                           fillOpacity: 0.35,
                           center: markerCenter,
                           radius: %d,
                           title: '%s',
                           map: map
                           });""" % (self.markerNumber,
                                     self.siteAnnotation.getLat(),
                                     self.siteAnnotation.getLon(),
                                     self.siteAnnotation.getBorderColor(),
                                     self.siteAnnotation.getColor(),
                                     self.siteAnnotation.getRadius(),
                                     self.siteAnnotation.getTitle())
        elif(shape == "rectangle"):
            delta = self.siteAnnotation.getRadius() / 100000;
            north = self.siteAnnotation.getLat() + (delta * 0.75);
            south = self.siteAnnotation.getLat() - (delta * 0.75);
            east = self.siteAnnotation.getLon() + delta;
            west = self.siteAnnotation.getLon() - delta;
            s0 = """ function create_marker_%d() {
              var markerCenter = new google.maps.LatLng(%f, %f);
              marker = new google.maps.Rectangle({
                         strokeColor: '%s',
                         strokeOpacity: 0.8,
                         strokeWeight: 2,
                         fillColor: '%s',
                         fillOpacity: 0.35,
                         bounds: {
                           north: %f,
                           south: %f,
                           east: %f,
                           west: %f},
                         title: '%s',
                         map: map
                         });""" % (self.markerNumber,
                                   self.siteAnnotation.getLat(),
                                   self.siteAnnotation.getLon(),
                                   self.siteAnnotation.getBorderColor(),
                                   self.siteAnnotation.getColor(),
                                   north, south, east, west,
                                   self.siteAnnotation.getTitle())
        html = self.createPopupContent()

        s1 = """
            var markup = `%s`
            """  %  html

        s2 = """
           infoWindow%d = new google.maps.InfoWindow({
                content: markup
               });
            google.maps.event.addListener(infoWindow%d, 'domready', function() {
              $("#infoWindow%d_tabs").tabs();
              $("a[href='#tab_0']").click()
              });

           google.maps.event.addListener(marker, 'click', function (){
              if(currentInfoWindow != null)
                 currentInfoWindow.close()
              infoWindow%d.setPosition(markerCenter);
              infoWindow%d.open(map);
              currentInfoWindow = infoWindow%d;
              });
         } """ % (self.markerNumber, self.markerNumber, self.markerNumber, self.markerNumber, self.markerNumber, self.markerNumber)

        return(s0 + s1 + s2)

    #------------------------------------------------------------------------------------------------------------------------
    def createPopupContent(self):

      anno = self.siteAnnotation
      htmlDoc = Doc()
      #pdb.set_trace()
      tabNumber = 1  # always an overview tab
      notesTabNeeded = 0
      if(len(anno.notesFile) > 0):
          notesTabNeeded = 1
      photoTabsNeeded = len(anno.photoTabs)
      videoTabsNeeded = len(anno.videoTabs)

      tabList = [{"type": "overview", "title": "Overview", "content": "overview goes here"}]
      if(notesTabNeeded):
          tabList.append({"type": "notes", "title": "Notes", "content": anno.notesFile})
      for i in range(photoTabsNeeded):
          tabList.append({"type": "photo", "title": anno.photoTabs[i]["title"], "content": anno.photoTabs[i]})
      for i in range(videoTabsNeeded):
          tabList.append({"type": "video", "title": anno.videoTabs[i]["title"], "content": anno.videoTabs[i]})

      with htmlDoc.tag("div", id="infoWindow%d_tabs" % self.markerNumber, klass="infoWindowTab"):
         with htmlDoc.tag("ul"):
             for tabNumber in range(len(tabList)):
                with htmlDoc.tag("li"):
                    with htmlDoc.tag("a", href="#tab_%d" % tabNumber):
                       htmlDoc.text(tabList[tabNumber]["title"])

         for tabNumber in range(len(tabList)):
            with htmlDoc.tag("div", id="tab_%d" % tabNumber):
               tabType = tabList[tabNumber]["type"]
               if(tabType == "overview"):
                  self.createOverviewTabContent(htmlDoc)
               if(tabType == "notes"):
                  self.createNotesTabContent(htmlDoc)
               if(tabType == "photo"):
                  self.createPhotoTabContent(htmlDoc, tabList[tabNumber])
               if(tabType == "video"):
                  self.createVideoTabContent(htmlDoc, tabList[tabNumber])

      htmlText = indent(htmlDoc.getvalue())
      return(htmlText)

    #------------------------------------------------------------------------------------------------------------------------
    def createOverviewTabContent(self, htmlDoc):

       anno = self.siteAnnotation

       with htmlDoc.tag("h4"):
           htmlDoc.text(anno.title)
       with htmlDoc.tag("ul"):
            htmlDoc.line('li', 'First reported: %s' % anno.firstReported)
            htmlDoc.line('li', 'Last update: %s' % anno.lastUpdate)
            htmlDoc.line('li', 'lat: %f' % anno.lat)
            htmlDoc.line('li', 'lon: %f' % anno.lon)
            if(anno.area > 0):
               htmlDoc.line('li', 'area: %5.2f acres' % anno.area)
            htmlDoc.line('li', 'severity: %d' % anno.severity)
            if(len(anno.contact) > 0):
               htmlDoc.line('li', 'Current contact: %s' % anno.contact)


    #------------------------------------------------------------------------------------------------------------------------
    def createNotesTabContent(self, htmlDoc):

       anno = self.siteAnnotation
       fullPath = os.path.join(anno.directoryAbsolutePath, anno.notesFile)
       assert(os.path.exists(fullPath))
       text = open(fullPath).read()

       htmlDoc.asis(text)

    #------------------------------------------------------------------------------------------------------------------------
    def createPhotoTabContent(self, htmlDoc, tabInfo):

       anno = self.siteAnnotation
       title = tabInfo["content"]["title"]
       url = tabInfo["content"]["url"]

       with htmlDoc.tag("div"):
          htmlDoc.stag("img", src="%s" % url, height="600") #, width="700")

    #------------------------------------------------------------------------------------------------------------------------
    def createVideoTabContent(self, htmlDoc, tabInfo):

       anno = self.siteAnnotation
       title = tabInfo["content"]["title"]
       url = tabInfo["content"]["url"]

       #pdb.set_trace()
       with htmlDoc.tag("div"):
          htmlDoc.asis('<iframe src="%s"  height="500" width="500" frameborder="0" allowfullscreen></iframe>' % url)
          #htmlDoc.stag("iframe", src="%s" % url, height="500", frameborder="0" allowfullscreen="True")

     #'<iframe width="300" height="215" src="http://www.youtube.com/embed/vG4vr83Ffd4" frameborder="0" allowfullscreen></iframe>',

    #------------------------------------------------------------------------------------------------------------------------
    def toJavascriptFile(self, filename):
        text = self.toJavascript()
        # print("marker.py, toJavascriptFile, writing to %s", filename)
        f = open(filename, "w")
        f.write(text)
        f.close()


