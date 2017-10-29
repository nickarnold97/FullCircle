
      // Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.
      var map, infoWindow, tempCenter;
      var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; 
      var labelIndex = 0; 
      var yourLocation; 
      var userMarker = []; 
      var markerArray = []; 
      var directions = []; 
      var distance = 0; 


      function initMap() {

        //Instantiate a directions service. 
        var directionsService = new google.maps.DirectionsService; 
        //Create a renderer for directions and bind it to the map.
        var directionsDisplay = new google.maps.DirectionsRenderer({map:map}); 
        //Instantiate an info window to hold step text.
        var stepDisplay = new google.maps.InfoWindow; 
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 14
        });
        infoWindow = new google.maps.InfoWindow;
        // Try HTML5 geolocation.
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
            yourLocation = {lat:pos.lat,lng:pos.lng}; 
            addMarker(pos,map); 
            map.setCenter(pos);
          }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
          });
        } else {
          // Browser doesn't support Geolocation
          handleLocationError(false, infoWindow, map.getCenter());
        }

        
        google.maps.event.addListener(map,'click',function(event){
          addMarker(event.latLng,map); 
          calculateAndDisplayRoute(directionsDisplay,directionsService,markerArray,stepDisplay,map); 
        })

        document.getElementById("loop").onclick = function(){makeLoop(directionsDisplay, directionsService,
          markerArray, stepDisplay, map)}; 

        //deleting all the directions that includes "destination is to your left" except for the last one
        for (var i = 0; i < directions.length-1; i++){
          if(directions[i].includes["destination"]){
            directions[i].remove(); 
          }
        }

      }

      function addMarker(location, map) {
        // Add the marker at the clicked location, and add the next-available label
        // from the array of alphabetical characters.
        var marker = new google.maps.Marker({
          position: location,
          label: labels[labelIndex++ % labels.length],
          map: map
        });
        userMarker.push(marker); 
      }

      function setMapOnAll(map){
        for(var i = 0; i < userMarker.length; i++){
          userMarker[i].setMap(map); 
        }
      }

      function clearMarkers(){
        setMapOnAll(null); 
      }

      function deleteMarkers(){
        clearMarkers();
        userMarker = []; 
        markerArray = [];  
        labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; 
        labelIndex = 0; 
        distance = 0; 
        document.getElementById('warnings-panel').innerHTML = '';
        initMap(); 
        directions = []; 
      }

      function makeLoop(directionsDisplay, directionsService,
          markerArray, stepDisplay, map){
        directionsService.route({
          origin: userMarker[userMarker.length-1].position,
          destination: userMarker[0].position,
          travelMode: "WALKING"
        },function(response,status){
          if (status == 'OK'){
            directionsDisplay = new google.maps.DirectionsRenderer({
              map:map,
              preserveViewport:true
            })
            directionsDisplay.setDirections(response); 
            showSteps(response,markerArray,stepDisplay,map); 
          } else {
            window.alert('Directions request failed due to ' + status); 
          }
        }); 
        distance += google.maps.geometry.spherical.computeDistanceBetween (userMarker[userMarker.length-2].position, userMarker[userMarker.length-1].position); 
<<<<<<< HEAD
        document.getElementById('warnings-panel').innerHTML = '<strong> Distance: <strong>' + Math.max(Math.round(distance/100)/10,0).toFixed(2) +' km'; 
=======
        document.getElementById('warnings-panel').innerHTML = '<b> Distance: ' + Math.round(distance/1000).toFixed(2) +' km</b>'; 
>>>>>>> de49055049dceab809c0c8ecfcd2648b6c6f6f46
      }

      function calculateAndDisplayRoute(directionsDisplay, directionsService,
          markerArray, stepDisplay, map) {
        // Retrieve the start and end locations and create a DirectionsRequest using
        // WALKING directions.
        directionsService.route({
          origin: userMarker[userMarker.length-2].position,
          destination: userMarker[userMarker.length-1].position,
          travelMode: 'WALKING'
        }, function(response, status) {
          // Route the directions and pass the response to a function to create
          // markers for each step.
          if (status === 'OK') {
            directionsDisplay = new google.maps.DirectionsRenderer({
              map:map,
              preserveViewport:true
            })
            directionsDisplay.setDirections(response);
            showSteps(response, markerArray, stepDisplay, map);
          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
        distance += google.maps.geometry.spherical.computeDistanceBetween (userMarker[userMarker.length-2].position, userMarker[userMarker.length-1].position);
        document.getElementById('warnings-panel').innerHTML = '<b> Distance: ' + Math.max(Math.round(distance/100)/10,0).toFixed(2)  +' km</b>';
      }

      function showSteps(directionResult, markerArray, stepDisplay, map) {
        // For each step, place a marker, and add the text to the marker's infowindow.
        // Also attach the marker to an array so we can keep track of it and remove it
        // when calculating new routes.
        var myRoute = directionResult.routes[0].legs[0];
        for (var i = 0; i < myRoute.steps.length; i++) {
          var marker = markerArray[i] = markerArray[i] || new google.maps.Marker;
          marker.setMap(map);
          marker.setPosition(myRoute.steps[i].start_location);
          attachInstructionText(
              stepDisplay, marker, myRoute.steps[i].instructions, map);
          if(!myRoute.steps[i].instructions.includes("destination"))
            directions.push(myRoute.steps[i].instructions); 
          }
      }

      function attachInstructionText(stepDisplay, marker, text, map) {
        google.maps.event.addListener(marker, 'click', function() {
          // Open an info window when the marker is clicked on, containing the text
          // of the step.
          stepDisplay.setContent(text);
          stepDisplay.open(map, marker);
        });
      }


      function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
        infoWindow.open(map);
      }
