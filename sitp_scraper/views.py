from django.http import JsonResponse

from .models import Route, BusStation, RouteStations


def get_routes(request):
    features = []
    for bus_station in BusStation.objects.all():
        print(bus_station, bus_station.longitude, bus_station.latitude)
        if bus_station.longitude and bus_station.latitude:
            features.append({
              "type": "Feature",
              "properties": {
                "marker-color": "#00608B",
                "marker-symbol": "bus",
                "marker-size": "small",
                "title": bus_station.name
              },
              "geometry": {
                "type": "Point",
                "coordinates": [
                  bus_station.longitude,
                  bus_station.latitude,
                ]
              }
            })

    return JsonResponse({
      "type": "FeatureCollection",
      "features": features,
    })
