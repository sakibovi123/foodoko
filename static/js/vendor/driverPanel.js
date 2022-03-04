let orderedUserLat = document.getElementById("ordered__userLat");
let orderedUserLong = document.getElementById("ordered__userLong");
let vendorLat = document.getElementById("vendor__lat");
let vendorLong = document.getElementById("vendor__long");
let totalDistance = document.getElementById("total__distance");

console.log(Number(orderedUserLat.value));
console.log(Number(orderedUserLong.value));
console.log(Number(vendorLat.value));
console.log(Number(vendorLong.value));

function getLocation() {
  // Ordered User

  var map;
  var directionsDisplay = new google.maps.DirectionsRenderer();
  var directionsService = new google.maps.DirectionsService();

  // var origin = new google.maps.LatLng(27.721503, 85.362072);
  // var destination = new google.maps.LatLng(27.711360, 85.318781)
  var origin = new google.maps.LatLng(Number(vendorLat.value), Number(vendorLong.value));
  var destination = new google.maps.LatLng(Number(orderedUserLat.value), Number(orderedUserLong.value))

  let mapOptions = {
    zoom: 18,
    center: origin,
  }

  map = new google.maps.Map(document.getElementById("driverPanelMap"), mapOptions);

  // For displaying direction
  directionsDisplay.setMap(map);

  var request = {
    origin: origin,
    destination: destination,
    travelMode: "DRIVING"
  }

  directionsService.route(request, function(result, status) {
    if (status === "OK") {
      // Showing direction
      directionsDisplay.setDirections(result);

      const distance = google.maps.geometry.spherical.computeDistanceBetween(origin, destination);
      console.log(distance);
      const getDistance = distance / 1000;
      totalDistance.innerText = Number(getDistance.toFixed(2));
    }
  })
}

setTimeout(() => {
  if (orderedUserLat &&
    orderedUserLong &&
    vendorLat &&
    vendorLong)
    getLocation();
  else {
    console.error("ERROR!");
  }
}, 1000);
