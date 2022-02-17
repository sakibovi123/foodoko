const mapIcon = document.getElementById("map-icon");

mapIcon.addEventListener("click", userLocation);

function initMap() {
    var mapFirst = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 23.6850, lng: 90.3563},
      zoom: 10
    });
    var input = document.getElementById('searchInput');
    mapFirst.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', mapFirst);

    var infowindow = new google.maps.InfoWindow();
    var markerFirst = new google.maps.Marker({
        map: mapFirst,
        anchorPoint: new google.maps.Point(0, -17)
    });

    autocomplete.addListener('place_changed', function() {
        infowindow.close();
        markerFirst.setVisible(false);
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("Autocomplete's returned place contains no geometry");
            return;
        }
  
        // If the place has a geometry, then present it on a map.
        if (place.geometry.viewport) {
            mapFirst.fitBounds(place.geometry.viewport);
        } else {
            mapFirst.setCenter(place.geometry.location);
            mapFirst.setZoom(17);
        }
        // markerFirst.setIcon(({
        //     url: place.icon,
        //     size: new google.maps.Size(71, 71),
        //     origin: new google.maps.Point(0, 0),
        //     anchor: new google.maps.Point(17, 34),
        //     scaledSize: new google.maps.Size(35, 35)
        // }));
        markerFirst.setPosition(place.geometry.location);
        markerFirst.setVisible(true);
    
        // var address = '';
        // if (place.address_components) {
        //     address = [
        //       (place.address_components[0] && place.address_components[0].short_name || ''),
        //       (place.address_components[1] && place.address_components[1].short_name || ''),
        //       (place.address_components[2] && place.address_components[2].short_name || '')
        //     ].join(' ');
        // }
    
        // infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
        // infowindow.open(mapFirst, markerFirst);
      
        // Location details
        // for (var i = 0; i < place.address_components.length; i++) {
        //     if(place.address_components[i].types[0] == 'postal_code'){
        //         document.getElementById('postal_code').innerHTML = place.address_components[i].long_name;
        //     }
        //     if(place.address_components[i].types[0] == 'country'){
        //         document.getElementById('country').innerHTML = place.address_components[i].long_name;
        //     }
        // }
        // document.getElementById('location').innerHTML = place.formatted_address;
        // document.getElementById('lat').innerHTML = place.geometry.location.lat();
        // document.getElementById('lon').innerHTML = place.geometry.location.lng();
    });
}


function userLocation(event){
    event.preventDefault()
    x = navigator.geolocation;

  		x.getCurrentPosition(success, failure);

  		function success(position)

  		{
  			var myLat = position.coords.latitude;
  			var myLong = position.coords.longitude;

  			//alert(myLat);

  			var coords = new google.maps.LatLng(myLat,myLong);

  			var mapOptions = {

  				zoom:18,
  				center: coords,
  				mapTypeId: google.maps.MapTypeId.ROADMAP
  			}

  			var mapMain = new google.maps.Map(document.getElementById("map"), mapOptions);
  			var markerOne = new google.maps.Marker({map:mapMain, position:coords});	
  		}

  		function failure(){ }
}


// modal
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
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