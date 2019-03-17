# generate the following javascript function, with embedded HTML, from a SiteAnnotation object
#------------------------------------------------------------------------------------------------------------------------
from yattag import *
import pdb
#------------------------------------------------------------------------------------------------------------------------
class Marker:

    siteAnnotation = None
    markerNumber = None

    def __init__(self, siteAnnotation, markerNumber):
       self.siteAnnotation = siteAnnotation
       self.markerNumber = markerNumber

    #------------------------------------------------------------------------------------------------------------------------
    def toJavascript(self):

        s0 = """ function create_marker_%d() {
           var markerLat = %f;
           var markerLon = %f;
           var markerCenter = new google.maps.LatLng(markerLat, markerLon);
           marker = new google.maps.Circle({
                      strokeColor: '#FF0000',
                      strokeOpacity: 0.8,
                      strokeWeight: 2,
                      fillColor: '#FFAAAA',
                      fillOpacity: 0.35,
                      center: markerCenter,
                      radius: %d,
                      title: '%s',
                      map: map
                      });""" % (self.markerNumber,
                                self.siteAnnotation.getLat(),
                                self.siteAnnotation.getLon(),
                                self.siteAnnotation.getRadius(),
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
      summaryTabsNeeded = 0
      if(len(anno.summaryTextFile) > 0):
          summaryTabsNeeded = 1
      photoTabsNeeded = len(anno.photoTabs)
      videoTabsNeeded = len(anno.videoTabs)

      tabList = [{"type": "overview", "content": "overview goes here"}]
      if(summaryTabsNeeded):
          tabList.append({"type": "summary", "content": anno.summaryTextFile})
      for i in range(photoTabsNeeded):
          tabList.append({"type": "photo", "content": anno.photoTabs[i]})
      for i in range(videoTabsNeeded):
          tabList.append({"type": "video", "content": anno.videoTabs[i]})

      with htmlDoc.tag("div", id="infoWindow%d_tabs" % self.markerNumber, klass="infoWindowTab"):
         with htmlDoc.tag("ul"):
             for tabNumber in range(len(tabList)):
                with htmlDoc.tag("li"):
                    with htmlDoc.tag("a", href="#tab_%d" % tabNumber):
                       htmlDoc.text(tabList[tabNumber]["type"])

         for tabNumber in range(len(tabList)):
            with htmlDoc.tag("div", id="tab_%d" % tabNumber):
               tabType = tabList[tabNumber]["type"]
               if(tabType == "overview"):
                  htmlDoc.text(tabList[tabNumber]["content"])
               if(tabType == "summary"):
                  htmlDoc.text(tabList[tabNumber]["content"])
               if(tabType == "photo"):
                  htmlDoc.text(tabList[tabNumber]["content"]["title"])
               if(tabType == "video"):
                  htmlDoc.text(tabList[tabNumber]["content"]["title"])


      htmlText = indent(htmlDoc.getvalue())
      return(htmlText)


    #------------------------------------------------------------------------------------------------------------------------
    def newCreatePopupContent(self):

      anno = self.siteAnnotation

    #------------------------------------------------------------------------------------------------------------------------
    def toJavascriptFile(self, filename):
        text = self.toJavascript()
        f = open(filename, "w")
        f.write(text)
        f.close()


