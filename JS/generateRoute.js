
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
      var halfWayPoint; 
      var distance; 
      var marker1; 
      var marker2; 
<<<<<<< HEAD
      var phoneNumber; 

      var domainString = document.domain;
      console.log(domainString);

      AWS.config.update({
        region: "us-east-1",
        // accessKeyId default can be used while using the downloadable version of DynamoDB. 
        // For security reasons, do not store AWS Credentials in your files. Use Amazon Cognito instead.
        accessKeyId: "AKIAIT26CPULRDUETWTA",
        // secretAccessKey default can be used while using the downloadable version of DynamoDB. 
        // For security reasons, do not store AWS Credentials in your files. Use Amazon Cognito instead.
        secretAccessKey: "GlIsJfCHlnz3Ha9RIwNd0IOfE7oHDJ4oZNbkKxSu"
      });

      function getQueryVariable(variable){
        var query = window.location.search.substring(1); 
        var vars = query.split("&"); 
        for(var i = 0; i < vars.length; i++){
          var pair = vars[i].split("="); 
          if(pair[0] == variable){return pair[1];}
        }
        return(false); 
      }
      phoneNumber = getQueryVariable("id"); 

      var ddb = new AWS.DynamoDB({apiVersion:'2012-10-08'}); 
      var params = {
        TableName : 'UserData',
        Key: {
          'Phonenumber': {
            S: "+16176948759",
          }
        }
      }; 

      ddb.getItem(params,function(err,data){
        if(err){
          console.log("Error",err);
        } else {
          console.log("Success",data); 
        }
        distance = data.Item.Distance.S; 
        console.log(distance);
        console.log(data.Item.Name.S); 
        document.getElementById("retrieve-alert").innerHTML = '<strong> Hello ' + data.Item.Name.S + '</strong>, you will run ' + distance + ' km '; 
      }); 


      function initMap() {
        // distance = prompt("How many kilometers are you running?")
=======


      function initMap() {
        distance = prompt("How many kilometers are you running?")
>>>>>>> de49055049dceab809c0c8ecfcd2648b6c6f6f46
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
            var halfLongitude = (distance/2)/111; 
            halfWayPoint = {lat:pos.lat,lng:pos.lng+halfLongitude}; 
            addMarker(halfWayPoint,map);  
            map.setCenter(pos);
          }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
          });
        } else {
          // Browser doesn't support Geolocation
          handleLocationError(false, infoWindow, map.getCenter());
        }

        //deleting all the directions that includes "destination is to your left" except for the last one
        for (var i = 0; i < directions.length-1; i++){
          if(directions[i].includes["destination"]){
            directions[i].remove(); 
          }
        }
        google.maps.event.addListener(map,'click',function(event){
          calculateAndDisplayRoute(directionsDisplay,directionsService,markerArray,stepDisplay,map);
          calculateAndDisplayRouteReverse(directionsDisplay, directionsService,
          markerArray, stepDisplay, map);  
        }) 
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
<<<<<<< HEAD
=======
        if(userMarker.length){
          alert("pushed");
          alert(marker.position);  
        }
>>>>>>> de49055049dceab809c0c8ecfcd2648b6c6f6f46
      }
  

      function calculateAndDisplayRoute(directionsDisplay, directionsService,
          markerArray, stepDisplay, map) {
        // Retrieve the start and end locations and create a DirectionsRequest using
        // WALKING directions.
<<<<<<< HEAD
=======
        if(!userMarker.length){
          alert("userMarker is not there"); 
        }
>>>>>>> de49055049dceab809c0c8ecfcd2648b6c6f6f46
        directionsService.route({
          origin: userMarker[0].position,
          destination: userMarker[1].position,
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

      }

    function calculateAndDisplayRouteReverse(directionsDisplay, directionsService,
          markerArray, stepDisplay, map) {
        // Retrieve the start and end locations and create a DirectionsRequest using
        // WALKING directions.
        if(!userMarker.length){
          alert("userMarker is not there"); 
        }
        directionsService.route({
          origin: userMarker[1].position,
          destination: userMarker[0].position,
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
