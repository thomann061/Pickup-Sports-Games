// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
var map, infoWindow, games;
function initMap() {

// Try HTML5 geolocation.
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
    var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
    };

    map = new google.maps.Map(document.getElementById('map'), {
        center: pos,
        zoom: 12
    });
    infoWindow = new google.maps.InfoWindow;

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
                            title: element['gameVenue']
                        });

                        var infoWindow = new google.maps.InfoWindow({
                            content: 
                                'Type: ' + element['gameType'] + '<br>' +
                                'Venue: ' + element['gameVenue'] + '<br>' +
                                'Address: ' + element['gameAddress'] + ', ' + element['gameCity'] + ', ' + element['gameState']
                                + element['gameZip'] +'<br>'
                                + 'Date/Time: ' + element['gameDateTime'] + '<br>'
                                + '<input type="button" id="' + element['id'] + '" value="Join Game" class="join-game btn btn-success">'
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

    }, function() {
        handleLocationError(true, infoWindow, map.getCenter());
    });

} else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
}

// Add ajax call to join-game button
$(document).on('click', '.join-game', function() {
    var id = $(this).attr('id');
    $.ajax({
        headers: { "X-CSRFToken": getCookie('csrftoken') },
        url: '/join-game',
        method: 'POST',
        dataType: 'json',
        data: {'gameId': id},
        success: function(data) {
            
        },
        error: function(data) {
            console.log(data);
        }
    });
});

function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}

}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
infoWindow.setPosition(pos);
infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
infoWindow.open(map);
}


