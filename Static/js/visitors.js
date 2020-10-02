/* global L, $, countries, visitors, Chart */


// create map:  
var folium_map_1 = L.map(
  "folium_map_1", {
    center: [0.0, 0.0],
    crs: L.CRS.EPSG3857,
    zoom: 3,
    zoomControl: true,
    preferCanvas: false,
  }
);

// create base layer:
var base_layer = L.tileLayer(
  "https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.jpg", {
    "attribution": "Map tiles by \u003ca href=\"http://stamen.com\"\u003eStamen Design\u003c/a\u003e, under \u003ca href=\"http://creativecommons.org/licenses/by/3.0\"\u003eCC BY 3.0\u003c/a\u003e. Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://creativecommons.org/licenses/by-sa/3.0\"\u003eCC BY SA\u003c/a\u003e.", 
    "detectRetina": false, 
    "maxNativeZoom": 18, 
    "maxZoom": 18, 
    "minZoom": 0, 
    "noWrap": false, 
    "opacity": 1, 
    "subdomains": "abc", 
    "tms": false
  }
).addTo(folium_map_1);


for (var visitor of visitors) {

  // create circle marker:    
  var circle_marker_1 = L.circleMarker(
    [visitor.nearest_latitude, visitor.nearest_longitude], {
      "bubblingMouseEvents": true, 
      "color": "#3186cc", 
      "dashArray": null, 
      "dashOffset": null, 
      "fill": true, 
      "fillColor": "#3186cc", 
      "fillOpacity": 0.2, 
      "fillRule": "evenodd", 
      "lineCap": "round", 
      "lineJoin": "round", 
      "opacity": 1.0, 
      "radius": 100*visitor.sigmoid_ratio, 
      "stroke": true, 
      "weight": 3
    }
  ).addTo(folium_map_1);

  // populate popup:
  var html_1 = $(`<div id="html_1" style="width: 100.0%; height: 100.0%;"> </div>`)[0];
  
  if (visitor.count == 1) html_1.innerHTML = '1 hit near ' + visitor.city;
  else html_1.innerHTML = visitor.count + ' hits near ' + visitor.city;
  
  // create popup:
  var popup_1 = L.popup({"maxWidth": "100%"});

  // add content to popup, popup to circle marker:
  popup_1.setContent(html_1); 
  circle_marker_1.bindPopup(popup_1);
}


// get chart element:
var ctx = document.getElementById('myChart');
ctx.height = '30%';

// plot data:
var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: countries.map(function(x){return x.name}),
    datasets: [{
      label: 'Number of Hits',
      data: countries.map(function(x){return x.count}),
      backgroundColor: [
        '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0',
        '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0',
        '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0',
        '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0',
        '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0', '#f0d5c0',
      ],
      borderColor: [
        'white', 'white', 'white', 'white', 'white', 'white',
        'white', 'white', 'white', 'white', 'white', 'white',
        'white', 'white', 'white', 'white', 'white', 'white',
        'white', 'white', 'white', 'white', 'white', 'white',
        'white', 'white', 'white', 'white', 'white', 'white',
      ],
      borderWidth: 1
    }]
  },
  options : {
    legend: {
      labels: {
        fontColor: '4d0000'
      }
    },
    scales: {
      xAxes: [{
        gridLines: {
          display:false
        },
        ticks: {
          fontColor: '4d0000',
        }
      }],
      yAxes: [{
        gridLines: {
          display:false
        },
        ticks: {
          fontColor: '4d0000',
        }
      }]
    }
  }
});