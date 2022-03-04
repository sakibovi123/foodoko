const mapIcon = document.getElementById("map-icon");

let userAddress = document.getElementById("user__address");
let userAddressVal = document.getElementById("user__addressVal");
let currentUserLat = document.getElementById("user__lat");
let currentUserLong = document.getElementById("user__long");

function initMap() {
  // console.log("I am triggered!");
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -33.8688, lng: 151.2195},
    zoom: 13
  });
  var input = document.getElementById('map__input');
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

  var autocomplete = new google.maps.places.Autocomplete(input);
  autocomplete.bindTo('bounds', map);

  var infowindow = new google.maps.InfoWindow();
  var marker = new google.maps.Marker({
      map: map,
      anchorPoint: new google.maps.Point(0, -29)
  });

  autocomplete.addListener('place_changed', function() {
      infowindow.close();
      marker.setVisible(false);
      var place = autocomplete.getPlace();
      if (!place.geometry) {
          window.alert("Autocomplete's returned place contains no geometry");
          return;
      }

      // If the place has a geometry, then present it on a map.
      if (place.geometry.viewport) {
          map.fitBounds(place.geometry.viewport);
      } else {
          map.setCenter(place.geometry.location);
          map.setZoom(17);
      }
      marker.setIcon(({
          url: place.icon,
          size: new google.maps.Size(71, 71),
          origin: new google.maps.Point(0, 0),
          anchor: new google.maps.Point(17, 34),
          scaledSize: new google.maps.Size(35, 35)
      }));
      marker.setPosition(place.geometry.location);
      marker.setVisible(true);
  
      var address = '';
      if (place.address_components) {
          address = [
            (place.address_components[0] && place.address_components[0].short_name || ''),
            (place.address_components[1] && place.address_components[1].short_name || ''),
            (place.address_components[2] && place.address_components[2].short_name || '')
          ].join(' ');
      }
  
      infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
      infowindow.open(map, marker);
  });
}

function userLocation(){
    const loc = navigator.geolocation;
    loc.getCurrentPosition(success, failure);

    function success(position) {
      let userLat = position.coords.latitude;
      let userLong = position.coords.longitude;

      console.log(typeof userLat)

      // console.log(userLat, userLong);

      currentUserLat.value = userLat;
      currentUserLong.value = userLong;

      let coords = new google.maps.LatLng(userLat, userLong);

      let mapOptions = {
        zoom: 18,
        center: coords,
        draggable: true,
      }

      let map = new google.maps.Map(document.getElementById("map"), mapOptions);
      let marker = new google.maps.Marker({map: map, position: mapOptions.center, draggable: true});

      let geocoder = new google.maps.Geocoder();
      geocoder.geocode({latLng: marker.getPosition()}, function(result, status) {
        // console.log(result);
        if (status === "OK") {
          // console.log(result[0].formatted_address); // --> Formatted address
          userAddress.value = result[0].formatted_address;
          userAddressVal.innerText = result[0].formatted_address;
          userAddressVal.classList.remove("d-none");
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
            userAddressVal.classList.remove("d-none");
          }
        })
      })
    }

    function failure() {
      console.error("Cannot detect your location! Please try again...");
    }
}


// modal
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
// var btn = document.getElementById("myBtn");
let btn = document.getElementById("myBtn"); // Edit

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
  userLocation();
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}