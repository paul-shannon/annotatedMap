# generate the following javascript function, with embedded HTML, from a SiteAnnotation object
#------------------------------------------------------------------------------------------------------------------------
from yattag import *
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
            var markup = '%s'
            """  %  html

        s2 = """
           infoWindow%d = new google.maps.InfoWindow({
                content: markup
               });
            google.maps.event.addListener(infoWindow%d, 'domready', function() {
              $("#infoWindow%d_tabs").tabs();
              $("a[href='#tab_1']").click()
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
      with htmlDoc.tag("div", id="infoWindow%d_tabs" % self.markerNumber, klass="infoWindowTab"):
         htmlDoc.text(anno.title)

      htmlText = htmlDoc.getvalue()
      return(htmlText)


      # content = """
      #       `<div id='infoWindow%d_tabs' class='infoWindowTab'>
      #             <ul>
 # 		    <li><a href='#tab_1'>DESCRIPTION</a>
 # 		    <li><a href='#tab_2'>Video</a>
 # 		    <li><a href='#tab_3'>Photo</a>
 #                   </ul>
 #                 <div id='tab_1'>
 #                  <ul>
 # 		   <li><b> Name:<b> <i> %s</i>
 # 		   <li><b> Date of first report:<b> <i> 23 oct 201%d</i>
 # 		   <li><b> Status: <b> <i> tentative die-off, to be confirmed next May</i>
 # 		   <li><b> Size:<b> <i> 1/4 acre</i>
 # 		   <li> <a href='nytimes.com'>More info</a>
 # 		 </ul>
 # 		</div>
 #                <div id='tab_2'>
 #                <iframe width='470' height='230' src='http://www.youtube.com/embed/vG4vr83Ffd4' frameborder='0' allowfullscreen></iframe>
 # 		</div>
 #                <div id='tab_3'>
 #                <img src='https://www.systemsbiology.org/wp-content/uploads/paul-shannon-web-300x300.jpg'>
 # 		</div>
 #                </div>`
 #               """ % (self.markerNumber, anno.title, self.markerNumber)
#
#       return(content)

    #------------------------------------------------------------------------------------------------------------------------
    def newCreatePopupContent(self):

      anno = self.siteAnnotation

    #------------------------------------------------------------------------------------------------------------------------
    def toJavascriptFile(self, filename):
        text = self.toJavascript()
        f = open(filename, "w")
        f.write(text)
        f.close()


