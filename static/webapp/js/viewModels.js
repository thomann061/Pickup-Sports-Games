


/**
 * Display a message at the top of the window
 * for 5 seconds.
 */
function display_message(text, status) {
    if( !document.getElementById('message') ) {
        var div = document.createElement('div');
        div.id = 'message';
        $('#message-wrapper').append(div);
    }
    $('#message-wrapper').hide();
    var css;
    if(status === "success") {
        $('#message').removeClass("bg-danger");
        css = "bg-success";
    } else {
        $('#message').removeClass("bg-success");
        css = "bg-danger";
    }
    $('#message').addClass(css);
    $('#message').text(text);
    $("#message-wrapper").fadeIn("slow").delay(3000).fadeOut("slow");
}

/**
 * Decorates a div with a map and adds marker points
 */

        // Create the map
var map, infoWindow, games, value, pos, markerList = new Array();

ko.bindingHandlers.googleMap = {
    init(mapDiv, valueAccessor, allBindingsAccessor) {

// Try HTML5 geolocation.
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
        pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };

        map = new google.maps.Map(document.getElementById('map'), {
            center: pos,
            zoom: 12
        });

    }, function() {
        handleLocationError(true, infoWindow, map.getCenter());
    });

} else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
infoWindow.setPosition(pos);
infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
infoWindow.open(map);
}


        //unwrap value
        value = valueAccessor();
        var valueUnwrapped = ko.utils.unwrapObservable(value);

        // declare geocoder
        var geocoder = new google.maps.Geocoder();

        valueUnwrapped.forEach(function(element) {
            
            var address = element.gameLocation(); 

            geocoder.geocode( {'address': address}, function(results, status) {
                // If everything went well
                if(status == 'OK') {
                    // create a marker
                    var marker = new google.maps.Marker({
                        position: results[0].geometry.location,
                        title: element.gameVenue(),
                        draggable: true
                    });
                    
                    // set an id for the marker
                    marker.set("id", element.gameId());

                    // add markers to a list
                    markerList.push(marker);

                    // create an info window
                    var infoWindow = new google.maps.InfoWindow({
                        content: 
                            '<h6>' + element.gameType() + '</h6>' +
                            '<input id="' + element.gameId() + '-game" type="button" value="More Info" class="btn btn-primary button-game-detail">'
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
}

/**
 * Will show updated game detail
 */
function show_game_detail() {
    // id is in this format - 'game-1'
    var value = $('.button-game-detail').attr('id');
    var valueList = value.split("-");
    var id = valueList[0];
    console.log(id);
    var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    $.ajax({
        headers: { "X-CSRFToken": token },
        url: '/api/games/' + id + '/users/',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            console.log(data);
            var game = data[0].game_info;

            // Create HTML for Game Detail
            var div = document.createElement('div');
            var divInner = document.createElement('div');
            var title = document.createElement('h5');
            var input = document.createElement('input');
            var userTitle = document.createElement('h6');
            div.classList.add('row');
            div.classList.add('row-main');
            divInner.classList.add('justify-content-between');
            divInner.classList.add('row');
            input.classList.add('btn', 'col', 'btn-success', 'button-join-game');
            input.setAttribute('type', 'button');
            input.setAttribute('value', 'Join Game');
            input.setAttribute('id', id);
            title.innerText = "Game Detail";
            title.classList.add('col');
            userTitle.innerText = "Players: " + data.length;
            var p1 = document.createElement('span');
            p1.innerText = 'Organizer: ' + game.gameOrganizer;
            var p2 = document.createElement('span');
            p2.innerText = 'Type: ' + game.gameType;
            var p3 = document.createElement('span');
            p3.innerText = 'Venue: ' + game.gameVenue;
            var p4 = document.createElement('span');
            p4.innerText = 'Address: ' + game.gameAddress + ", " + game.gameCity + ", " + game.gameState + " " + game.gameZip;            
            var p5 = document.createElement('p');
            p5.innerText = 'Date, Time: ' + game.gameDateTime;
            div.appendChild(divInner);
            divInner.appendChild(title);
            divInner.appendChild(input);
            div.appendChild(p1);
            div.appendChild(p2);
            div.appendChild(p3);
            div.appendChild(p4);
            div.appendChild(p5);
            div.appendChild(userTitle);
            // Add users to detail
            var users;
            data.forEach(function(element) {
                var usersName = element.user_info.first_name + " " + element.user_info.last_name;
                var span = document.createElement('span');
                span.innerText = usersName;
                div.appendChild(span);
            });

            //remove game detail if already there
            if( $('#gameDetail div') ) {
                $('#gameDetail div').remove();
            } 
            //append game detail
            $('#gameDetail').hide().html(div).fadeIn("slow");
        },
        error: function(data) {

        }
    });
}

// Add click event to show game detail
$(document).on('click', '.button-game-detail', function() {
    show_game_detail();
});

// Add ajax call to join a game
$(document).on('click', '.button-join-game', function() {
    var id = $(this).attr('id');
    var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    var userId;
    $.getJSON( "/api/users/current", ( data ) => {
        userId = data[0].id;
        console.log("game: " + id + " user: " + userId);
        $.ajax({
            headers: { "X-CSRFToken": token },
            url: '/api/gameusers/',
            method: 'POST',
            dataType: 'json',
            data: {'game': id, 'user': userId },
            success: function(data, status, request) {
                if(request.status === 201)
                    display_message("You joined " + data.user_info['first_name'] + "'s game.", "success");
                    show_game_detail();
            },
            error: function(data, status) {
                console.log(status);
                if(status === "error")
                    display_message("You already joined this game.", "error");
            }
        });
    });
});

/**
 * Save a game
 */
$(document).on('click', '.button-save-game', function() {
    var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    var userId;
    $.getJSON( "/api/users/current", ( data ) => {
        userId = data[0].id;
        console.log("game: " + id + " user: " + userId);
        $.ajax({
            headers: { "X-CSRFToken": token },
            url: '/api/gameusers/',
            method: 'POST',
            dataType: 'json',
            data: {'game': id, 'user': userId },
            success: function(data) {

            },
            error: function(data) {

            }
        });
    });
});

// Game data model
const GamesViewModel = function(gameList) {

    const self = this;

    /**
     * Set an observable array with all the games
     */
    self.gameList = ko.observableArray(ko.utils.arrayMap(gameList, (game) => {
		return { 
            gameOrganizer: ko.observable(game.gameOrganizer),
		    gameType: ko.observable(game.gameType),
            gameVenue: ko.observable(game.gameVenue),
            gameLocation: ko.computed(function() {
                return game.gameAddress + ", " + game.gameCity + ", " +
                       game.gameState + " " + game.gameZip;
            }, this),
            gameDateTime: ko.observable(game.gameDateTime),
            gameId: ko.observable(game.id),
	    }
    }));

    /**
     * New Game Model
     */
    self.newGameModel = {
        gameOrganizer: ko.observable(),
        gameType: ko.observable(),
        gameVenue: ko.observable(),
        gameLocation: ko.observable(),
        gameDateTime: ko.observable()
    }

    /**
     * Add New Game
     */
    self.newGame = function() {
        // Create HTML for New Game Detail
        var div = document.createElement('div');
        var divInner = document.createElement('div');
        var title = document.createElement('h5');
        var input = document.createElement('input');
        div.classList.add('row');
        div.classList.add('row-main');
        divInner.classList.add('justify-content-between');
        divInner.classList.add('row');
        input.classList.add('btn', 'col', 'btn-success', 'button-save-game');
        input.setAttribute('type', 'button');
        input.setAttribute('value', 'Save');
        title.innerText = "New Game";
        title.classList.add('col');
        div.appendChild(divInner);
        divInner.appendChild(title);
        divInner.appendChild(input);
        var p1 = document.createElement('input'),
            p2 = document.createElement('input'),
            p3 = document.createElement('input'),
            p4 = document.createElement('input'),
            p5 = document.createElement('input'),
            label1 = document.createElement('label'),
            label2 = document.createElement('label'),
            label3 = document.createElement('label'),
            label4 = document.createElement('label'),
            label5 = document.createElement('label');
        var inputFieldList = [p1, p2, p3, p4, p5];
        var labelFieldList = [label1, label2, label3, label4, label5];
        // set name
        p1.setAttribute("name", "organizer");
        p2.setAttribute("name", "type");
        p3.setAttribute("name", "venue");
        p4.setAttribute("name", "location");
        p5.setAttribute("name", "dateTime");
        p1.setAttribute("name", "organizer");
        p2.setAttribute("name", "type");
        p3.setAttribute("name", "venue");
        p4.setAttribute("name", "location");
        p5.setAttribute("name", "dateTime");
        label1.setAttribute("for", "organizer");
        label2.setAttribute("for", "type");
        label3.setAttribute("for", "venue");
        label4.setAttribute("for", "location");
        label5.setAttribute("for", "dateTime");
        inputFieldList.forEach(function(el) {
            el.classList.add("form-control");
        });
        label1.innerHTML = "Organizer";
        label2.innerHTML = "Type";
        label3.innerHTML = "Venue";
        label4.innerHTML = "Location";
        label5.innerHTML = "Date, Time";
        for(var i = 0; i < inputFieldList.length; i++) {
            div.appendChild(labelFieldList[i])
            div.appendChild(inputFieldList[i]);
        }

        //remove game detail if already there
        if( $('#newGameDetail div') ) {
            $('#newGameDetail div').remove();
        } 
        //append game detail
        $('#newGameDetail').hide().html(div).fadeIn("slow");
    };
    

    /**
     * Delete a game.
     */
    self.deleteGame = function(game) {
    // if(self.checkOrganizer(game)) {
    console.log("deleting game...");
    //Token needed for session based auth
    var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    // Remove the game from the ui
    self.gameList.remove(game);
    // Additionally remove the game marker from the map
    // Traverse the markers
    markerList.forEach(function(marker) {
        // Find marker and delete it
        if(marker.id === game.gameId()) {
            marker.setMap(null);
        }
            
    });
    // return $.ajax({
    //     headers: {
    //         "X-CSRFToken": token
    //     },
    //     url: '/api/games/' + game.gameId(),
    //     type: 'DELETE',
    //     success: function(data) {
    //         //self.gameUserList.remove(game);
    //         self.gameList.remove(game);
    //     },
    //     error: function () {

        }
    // });

};


// // Game data model
// const myGamesModel = function(tempGameUserList) {

//     const self = this;

//     /**
//      * Set an observable array with current users games
//      */
//     self.gameUserList = ko.observableArray(ko.utils.arrayMap(tempGameUserList, (gameUser) => {
// 		return { 
//             gameUserId: ko.observable(gameUser.id),
//             gameOrganizer: ko.observable(gameUser.game_info.gameOrganizer),
// 		    gameType: ko.observable(gameUser.game_info.gameType),
//             gameVenue: ko.observable(gameUser.game_info.gameVenue),
//             gameLocation: ko.computed(function() {
//                 return gameUser.game_info.gameAddress + ", " + gameUser.game_info.gameCity + ", " + 
//                        gameUser.game_info.gameState + " " + gameUser.game_info.gameZip;
//             }, this),
//             gameDateTime: ko.observable(gameUser.game_info.gameDateTime),
//             gameId: ko.observable(gameUser.game),
//             userId: ko.observable(gameUser.user),
//             gameOrganizerId: ko.observable(gameUser.game_info.gameOrganizer)
// 	    }
//     }));

    // self.message = ko.observable();

    // self.createGame = function(game) {
	// 	return $.ajax({
	// 		url: '/api/games/',
	// 		type: 'POST',
	// 		success: function() {
	// 			self.gameUserList.add(game);
	// 		},
	// 		error: function () {

	// 		}
	// 	});
	// };

    // // self.checkOrganizer = function(game) {
    // //     console.log("user id..." + game.userId() + " " + "game organizer id..." + game.gameOrganizerId());
    // //     return game.userId() == game.gameOrganizerId();
    // // }

    // self.joinGame = function() {
    //     console.log("joining game...");
    //     // Add ajax call to join-game button
    //     var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    //     // $.ajax({
    //     //     headers: {
    //     //         "X-CSRFToken": token
    //     //     },
    //     //     url: '/join-game',
    //     //     method: 'POST',
    //     //     dataType: 'json',
    //     //     data: { 'gameId': id },
    //     //     success: function(data) {
    //     //         handle_messages(data);
    //     //         self.gameUserList.add(game);
    //     //     },
    //     //     error: function(data) {

    //     //     }
    //     // });
    // }


        // } else {
    //         console.log("deleting game user...");
    //         //Token needed for session based auth
    //         var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    //         return $.ajax({
    //             headers: {
    //                 "X-CSRFToken": token
    //             },
    //             url: '/api/gameusers/' + game.gameUserId(),
    //             type: 'DELETE',
    //             success: function(data) {
    //                 self.gameUserList.remove(game);
    //             },
    //             error: function () {

    //             }
    //         });
    //     }
	// };

/**
 * Load after dom is rendered.
 */
$(document).ready(function() {

    $.getJSON( "/api/games/", ( data ) => {
        const games = data;
        const model = new GamesViewModel(games);
        ko.applyBindings(model);
    });

});


