var map;
var markers = [];
var infowindows = [];
var popupcontent = "<table><col width='300px'/><tr><td><div style='vertical-align: top;text-align: left;font-size: x-large;font-weight: 600;'>Fix This Spot</div></td><td rowspan=2><img src='img/dumpyard.png' width='100px' style='border-style: solid;border-color: #A3A375 #A3A375;border-width: 1px;'/></td></tr><tr><td><p>Address.</p><p>Join Fix | Organize Fix</p></td></tr></table>";
function setLocation(city) {
    switch (city) {
    case "Chennai":
	panto = new google.maps.LatLng(13.0597050,80.2252280);
	break;
    case "Bangalore":
	panto = new google.maps.LatLng(12.9715990,77.5945630);
	break;
    case "Kolkata":
	panto = new google.maps.LatLng(22.5726460,88.3638950);
	break;
    case "Delhi":
	panto = new google.maps.LatLng(28.6353080,77.2249600);
	break;
    }
    map.panTo(panto);
}

function myLocation(position) {
    lat = position.coords.latitude;
    lng = position.coords.longitude;
}

function initialize() {
    map = new google.maps.Map(document.getElementById('map-canvas'), {
	center: new google.maps.LatLng(12.9715990,77.5945630),
	zoom: 8,
	mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    
    // Create the search box and link it to the UI element.
    var input = /** @type {HTMLInputElement} */(
	document.getElementById('pac-input'));
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    
    var searchBox = new google.maps.places.SearchBox(
	/** @type {HTMLInputElement} */(input));
    
    // Listen for the event fired when the user selects an item from the
    // pick list. Retrieve the matching places for that item.
    google.maps.event.addListener(searchBox, 'places_changed', function() {
	var places = searchBox.getPlaces();
	
	if (places.length == 0) {
	    return;
	}
	
	// For each place, get the icon, place name, and location.
	var bounds = new google.maps.LatLngBounds();
	for (var i = 0, place; place = places[i]; i++) {
	    bounds.extend(place.geometry.location);
	}
	// setting the bounds
	map.fitBounds(bounds);
	// set zoom level to sane level
	map.setZoom(16);
    });
    
    // Bias the SearchBox results towards places that are within the bounds of the
    // current map's viewport.
    google.maps.event.addListener(map, 'bounds_changed', function() {
	var bounds = map.getBounds();
	searchBox.setBounds(bounds);
    });
    // add click event
    google.maps.event.addListener(map, 'click', function(event) {
	// drop a marker at the click location
	document.getElementById('id_lat').value = event.latLng.lat();
	document.getElementById('id_lng').value = event.latLng.lng();
	document.getElementById('id_address').value = document.getElementById('pac-input').value;
	addMarker(event.latLng);
    });
}

// Add a marker to the map and push to the array.
function addMarker(location) {
    // close all open infowindows
    for (var i = 0; i < infowindows.length; i++) {
	infowindows[i].close();
    }
    var marker = new google.maps.Marker({
	position: location,
	draggable:true,
	map: map
    });
    markers.push(marker);
    // add left click event
    google.maps.event.addListener(markers[markers.length-1], 'click', function(event) {
	// close all open infowindows
	for (var i = 0; i < infowindows.length; i++) {
	    infowindows[i].close();
	}
	console.log(event.latLng.lat());
	// pop up info bar
	marker.setTitle('Pop up');
	var infowindow = new google.maps.InfoWindow({
	    content: popupcontent,
	    maxWidth: 400
	});
	infowindow.open(map, marker);
	infowindows.push(infowindow);
    });
    // add right click event
    google.maps.event.addListener(markers[markers.length-1], 'rightclick', function(event) {
	// delete the marker on right click
	marker.setMap(null);
    });
}

google.maps.event.addDomListener(window, 'load', initialize);
