// I would like to reference developers.google.com.
// I used part of their code for the javascript portion of the map and geocoder. 

// initialize the markers list, and also the info window and info content variables 
var markers = [];
var infowin;
var infowinContent;

// This function initializes the map and also sets up the info window and geocoder
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 3,
        center: {lat: 0, lng: 0}
    });

    // Creates the info window
    infowin = new google.maps.InfoWindow();
    infowinContent = document.getElementById('infowindow-content');
    infowin.setContent(infowinContent);

    // creates the geocoder
    var geocoder = new google.maps.Geocoder();
    // sets an onclick listener for the submit button
    document.getElementById('submit').addEventListener('click', function() {
        // calls the geocode address function to retrieve the geocode information
        geocodeAddress(geocoder, map);
        map.setZoom(6);
    });

}

// This functions gets the geocode information for the typed address
//  and sets a marker and also fills the info window content.
function geocodeAddress(geocoder, resultsMap) {
    var address = document.getElementById('address').value;
    geocoder.geocode({'address': address}, function(results, status) {
        // Makes sure that the response data is good
        if (status === 'OK') {
            // reset the markers because we only want 1 marker on the map at a time
            resetMarkers();
            resultsMap.panTo(results[0].geometry.location);
            // create the new marker by giving it a map and location
            var marker = new google.maps.Marker({
                map: resultsMap,
                position: results[0].geometry.location
            });
            // adds this new marker to the markers list.
            markers.push(marker);

            // This sections fills the info window with the correct information
            infowinContent.children['title'].textContent = address + ':';
            infowinContent.children['lat'].textContent = results[0].geometry.location.lat();
            infowinContent.children['lng'].textContent = results[0].geometry.location.lng();
            // and then open that info window
            infowin.open(resultsMap, marker);     
        } else {
            // if the response data had issues, alert those issues.
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}

// This function will delete all of the previous markers on the map.
function resetMarkers(){
    // Iterates through the list of markers and sets their maps to null.
    for(var i = 0; i < markers.length; i++){
        markers[i].setMap(null);
    }
    // Create a new empty list of markers
    markers = [];
}
