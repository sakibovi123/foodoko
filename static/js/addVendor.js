console.log("HELLO WORLD!");

let vendorUserAddress = document.getElementById("vendor__address");
let vendorUserLat = document.getElementById("vendor__userLat");
let vendorUserLong = document.getElementById("vendor__userLong");
let vendorTextArea = document.querySelector(".vendor__textarea");

function locationAddress() {
    const loc = navigator.geolocation;

    loc.getCurrentPosition(success, failure);

    function success (position) {
    let userLat = position.coords.latitude;
    let userLong = position.coords.longitude;

    // console.log(userLat, userLong);

    var marker, map;

    let coords = new google.maps.LatLng(userLat, userLong);

    let mapOptions = {
        zoom: 18,
        center: coords,
        draggable: true,
      }

    map = new google.maps.Map(document.getElementById("addVendorMap"), mapOptions);
    marker = new google.maps.Marker({map: map, position: mapOptions.center, draggable: true});

    let geocoder = new google.maps.Geocoder();
    geocoder.geocode({latLng: marker.getPosition()}, function(result, status) {
      // console.log(result);
      if (status === "OK") {
          console.log(result[0]);
        // console.log(result[0].formatted_address); // --> Formatted address
        vendorUserAddress.value = result[0].formatted_address;
        vendorTextArea.value = result[0].formatted_address;
        vendorUserLat.value = userLat;
        vendorUserLong.value = userLong;
        // vendorUserLat = 
      }
    })

    // Autocomplete
    var input = document.getElementById("add__vendorMapInput");
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    
    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo("bounds", map);

    var infoWindow = new google.maps.InfoWindow();
    marker = new google.maps.Marker({
        map: map,
        anchorPoint: new google.maps.Point(0, -29),
    });

    autocomplete.addListener("place_changed", function() {
        infoWindow.close();
        marker.setVisible(false);
        var place = autocomplete.getPlace();

        console.log(place);

        if (!place.geometry) {
            window.alert("Invalid geometry!");
            return;
        }

        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);
        }

        // marker.setIcon(({
        //     url: place.icon,
        //     size: new google.maps.Size(71, 71),
        //     origin: new google.maps.Point(0, 0),
        //     anchor: new google.maps.Point(17, 34),
        //     scaledSize: new google.maps.Size(35, 35)
        // }))

        marker.setPosition(place.geometry.location);

        // console.log(place.geometry.location.lat());
        // console.log(place.geometry.location.lng());

        // Saving address data
        vendorUserAddress.value = place.formatted_address
        vendorTextArea.value = place.formatted_address;
        vendorUserLat.value = place.geometry.location.lat();
        vendorUserLong.value = place.geometry.location.lng();
        
        marker.setVisible(true);
    });
}

    function failure() {
        alert("Sorry! Cannot get your address")
    }
}