from django.shortcuts import render
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")


# Create your views here.
def index(request):
    if request.method == 'POST':
        try:
            getText = request.POST.get('search')
            location = geolocator.geocode(getText)
            latitude, longitude = location.latitude, location.longitude
            return render(request, 'index.html', {'address': getText, 'street': location.address, 'latitude': latitude, 'longitude': longitude})
        except:
            print("Sorry Address Not Found")
    return render(request, 'index.html')