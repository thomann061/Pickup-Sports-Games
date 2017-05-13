// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
var map, infoWindow, games;
function initMap() {

map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 12
});
infoWindow = new google.maps.InfoWindow;

// Try HTML5 geolocation.
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
    var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
    };

    map.setCenter(pos);
    }, function() {
    handleLocationError(true, infoWindow, map.getCenter());
});

// Get the games
$.ajax({
    url: '/api/games/',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
        var geocoder = new google.maps.Geocoder();
        data.forEach(function(element) {
            var address = element['gameAddress'] + ', ' + element['gameCity'] + ', ' + element['gameState']
                            + element['gameZip']; 
            geocoder.geocode( {'address': address}, function(results, status) {
                if(status == 'OK') {
                    var marker = new google.maps.Marker({
                        position: results[0].geometry.location,
                        title: element['venue']
                    });
                    var infoWindow = new google.maps.InfoWindow({
                        content: 
                            '<div id="info-window">' + 
                            '<p>Type: ' + element['gameType'] + '</p>' +
                            '<p>Venue: ' + element['gameVenue'] + '</p>' +
                            '<p>Address: ' + element['gameAddress'] + ', ' + element['gameCity'] + ', ' + element['gameState']
                            + element['gameZip'] +'</p>'
                            + '<p>Date/Time: ' + element['gameDateTime'] + '</p>'
                            + '</div'
                    });
                    marker.addListener('click', function() {
                        infoWindow.open(map, marker);
                    });
                    marker.setAnimation(google.maps.Animation.DROP);
                    marker.setMap(map);
                } else {
                    // geocoding did not work, handle later
                }
            });
        });
    }
  });

} else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
}
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
infoWindow.setPosition(pos);
infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
infoWindow.open(map);
}
