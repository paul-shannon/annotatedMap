

var map;
var currentInfoWindow = null;
var marker1, marker2, infoWindow1, infoWindow2;
//----------------------------------------------------------------------------------------------------
function initializeMap()
{
   console.log("==== initialzing map")
   var iniLat = 47.5551369;
   var iniLon = -122.2553546;
   var iniZoom = 15;
   var mapCenter = new google.maps.LatLng(iniLat, iniLon);

   var mapOptions = {
       zoom: iniZoom, center: mapCenter, mapTypeId: google.maps.MapTypeId.ROADMAP
       }
   map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
   google.maps.event.addListener(map, 'tilesloaded', function () { createMarkers() });

   var myStyle = [{featureType: "administrative", elementType: "labels",    stylers: [{ visibility: "off" }]},
                  {featureType: "poi",            elementType: "labels",    stylers: [{ visibility: "off" }]},
                  {featureType: "water",          elementType: "labels",    stylers: [{ visibility: "off" }]},
                  {featureType: "road",           elementType: "labels",    stylers: [{ visibility: "off" }]},
                  {featureType: "road",           elementType: "geometry",  stylers: [{ visibility: "off" }]}
                 ];

   map.setOptions({styles: myStyle});

} // initializeMap
//----------------------------------------------------------------------------------------------------
function createMarkers()
{

  /**************
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

     //   '<span style="font-family: Trebuchet MS; font-size:10pt; color: maroon"><b>1</b>' +
     //   '<iframe width="300" height="215" src="http://www.youtube.com/embed/vG4vr83Ffd4" frameborder="0" allowfullscreen></iframe>'

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


   **********/
  var centerLat  =   47.55364950712636;
  var centerLong = -122.2468900680542;

  infoWindow2 = new google.maps.InfoWindow({
                 content:
                    '<span style="font-family: Trebuchet MS; font-size:10pt; color: maroon"><b>2</b>' +
                    '<iframe width="300" height="215" src="http://www.youtube.com/embed/vG4vr83Ffd4" frameborder="0" allowfullscreen></iframe>',
                 position: new google.maps.LatLng(centerLat, centerLong)
                 });

  var delta = 0.0005;

  locs = [new google.maps.LatLng(centerLat - delta, centerLong - delta),
          new google.maps.LatLng(centerLat - delta, centerLong + delta),
          new google.maps.LatLng(centerLat + delta, centerLong + delta),
          new google.maps.LatLng(centerLat + delta, centerLong - delta)]

  marker2 =  new google.maps.Polygon({
                  paths: locs,
                  strokeColor: '#0000FF',
                  strokeOpacity: 0.8,
                  strokeWeight: 2,
                  fillColor: '#AAAAFF',
                  fillOpacity: 0.35,
                  title: 'Compost Piles',
                  map: map
                  });

  google.maps.event.addListener(marker2, 'click', function (){
     if(currentInfoWindow != null)
        currentInfoWindow.close()
     infoWindow2.setPosition(new google.maps.LatLng(centerLat, centerLong));
     infoWindow2.open(map);
     currentInfoWindow = infoWindow2;
     });

  google.maps.event.addListener(map, "click", function(event){
     console.log(event.latLng.lat() + " " + event.latLng.lng());
     });

} // createMarkers
//----------------------------------------------------------------------------------------------------
$(document).ready(function() {
    console.log("ready!")
    initializeMap()
    console.log("==== map var, before calling createMarker_1: ")
    console.log(map)
    createMarker_1()
    })

