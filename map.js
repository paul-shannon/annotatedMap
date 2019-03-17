var map;
var currentInfoWindow = null;
// var marker1, marker2, infoWindow1, infoWindow2;
//----------------------------------------------------------------------------------------------------
function initializeMap()
{
   console.log("==== initialzing map")
   var initialLat = %f;
   var initialLon = %f;
   var initialZoom = %f;
   var mapCenter = new google.maps.LatLng(initialLat, initialLon);

   var mapOptions = {
       zoom: initialZoom, center: mapCenter, mapTypeId: google.maps.MapTypeId.ROADMAP
       }
   map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
   google.maps.event.addListener(map, 'tilesloaded', function(){createMarkers()});

   var myStyle = [{featureType: "administrative", elementType: "labels",    stylers: [{ visibility: "off" }]},
                  {featureType: "poi",            elementType: "labels",    stylers: [{ visibility: "off" }]},
                  {featureType: "water",          elementType: "labels",    stylers: [{ visibility: "off" }]},
                  {featureType: "road",           elementType: "labels",    stylers: [{ visibility: "off" }]},
                  {featureType: "road",           elementType: "geometry",  stylers: [{ visibility: "off" }]}
                 ];

   map.setOptions({styles: myStyle});

} // initializeMap
//----------------------------------------------------------------------------------------------------
$(document).ready(function() {
    console.log("ready!")
    initializeMap()
    })

