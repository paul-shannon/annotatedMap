// generate the following javascript function, with embedded HTML, from a SiteAnnotation object
//------------------------------------------------------------------------------------------------------------------------
function createMarker_1()
{
  var iniLat = 47.5551369;
  var iniLon = -122.2553546;
  var mapCenter = new google.maps.LatLng(iniLat, iniLon);

  marker1 = new google.maps.Circle({
                  strokeColor: '#FF0000',
                  strokeOpacity: 0.8,
                  strokeWeight: 2,
                  fillColor: '#FFAAAA',
                  fillOpacity: 0.35,
                  center: mapCenter,
                  radius: 20,
                  title: 'Fatnose',
                  map: map
                  });

  var markup = ['<div id="infoWindow1_tabs" class="infoWindowTab">',
                '  <ul>',
		'    <li><a href="#tab_1">Description</a>',
		'    <li><a href="#tab_2">Video</a>',
		'    <li><a href="#tab_3">Photo</a>',
                '  </ul>',
                '<div id="tab_1">',
                ' <ul>',
		'   <li><b> Name:<b> <i> name of site goes here</i>',
		'   <li><b> Date of first report:<b> <i> 23 oct 2017</i>',
		'   <li><b> Status: <b> <i> tentative die-off, to be confirmed next May</i>',
		'   <li><b> Size:<b> <i> 1/4 acre</i>',
		'   <li> <a href="nytimes.com">More info</a> ',
		' </ul>',
		'</div>',
                '<div id="tab_2">',
                '<iframe width="470" height="230" src="http://www.youtube.com/embed/vG4vr83Ffd4" frameborder="0" allowfullscreen></iframe>',
		'</div>',
                '<div id="tab_3">',
                '<img src="https://www.systemsbiology.org/wp-content/uploads/paul-shannon-web-300x300.jpg">',
		'</div>',
                '</div>'].join('');

  infoWindow1 = new google.maps.InfoWindow({
                   content: markup
                   });
   google.maps.event.addListener(infoWindow1, 'domready', function() {
     $("#infoWindow1_tabs").tabs();
     $("a[href='#tab_1']").click()
     });

  google.maps.event.addListener(marker1, 'click', function (){
     if(currentInfoWindow != null)
        currentInfoWindow.close()
     infoWindow1.setPosition(mapCenter);
     infoWindow1.open(map);
     currentInfoWindow = infoWindow1;
     });

}
//------------------------------------------------------------------------------------------------------------------------