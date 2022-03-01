let userAddress = document.getElementById("orderedUser__address");
let userAddressVal = document.getElementById("orderedUser__addressVal");

function getOrderedDestination() {
// For displaying direction
  // Ordered User
    const loc = navigator.geolocation;
    loc.getCurrentPosition(success, failure);

    function success(position) {
      // This is the vendor location
      let userLat = position.coords.latitude;
      let userLong = position.coords.longitude;

      // console.log(userLat, userLong);
      // Save userLat and userLong value
      let coords = new google.maps.LatLng(userLat, userLong);

      let mapOptions = {
        zoom: 18,
        center: coords,
        draggable: true,
      }

      let map = new google.maps.Map(document.getElementById("vendor__map"), mapOptions);
      let marker = new google.maps.Marker({map: map, position: mapOptions.center});

      let geocoder = new google.maps.Geocoder();
      geocoder.geocode({latLng: marker.getPosition()}, function(result, status) {
        // console.log(result);
        if (status === "OK") {
          // console.log(result[0].formatted_address); // --> Formatted address
          userAddress.value = result[0].formatted_address;
          userAddressVal.innerText = result[0].formatted_address;
        }
      })
      // --> Draggable marker event
      google.maps.event.addListener(marker, "dragend", function() {
        // console.log(marker.getPosition().lat());
        // console.log(marker.getPosition().lng());
        geocoder.geocode({latLng: marker.getPosition()}, function(result, status) {
          // console.log(result);
          if (status === "OK") {
            // console.log(result[0].formatted_address); // --> Formatted address
            userAddress.value = result[0].formatted_address;
            userAddressVal.innerText = result[0].formatted_address;
          }
        })
      })

      // For displaying direction
      // Vendor location
      var directionsDisplay = new google.maps.DirectionsRenderer();
      var directionsService = new google.maps.DirectionsService();

      var destinationPoint = new google.maps.LatLng(23.6850, 90.3563);
      directionsDisplay.setMap(map);

      var request = {
        origin: coords,
        destination: destinationPoint,
        travelMode: "DRIVING"
      }

      directionsService.route(request, function(result, status) {
        if (status === "OK") {
          console.log(result);
          directionsDisplay.setDirections(result);
        }
      })

      // Distance calcalution
      console.log(google.maps.geometry.spherical.computeDistanceBetween (coords, destinationPoint));

    }

    function failure() {
      console.error("Cannot detect your location! Please try again...");
    }
}

getOrderedDestination();