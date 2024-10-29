from django.shortcuts import render
import json
import urllib.request
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create your views here.

def home(request):
    if request.method == "POST":
        City = request.POST.get('city', 'True')
        api_key = os.getenv('OPENWEATHER_API_KEY')  # Get the API key from environment variables
        if api_key:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={City}&units=imperial&appid={api_key}'
            Source = urllib.request.urlopen(url).read()
            ListofData = json.loads(Source)
            context = {
                'City': City,
                'CountryCode': str(ListofData['sys']['country']),
                'Coordinates': str(ListofData['coord']['lon']) + ', ' + str(ListofData['coord']['lat']),
                'Temperature': str(ListofData['main']['temp']) + '°F',
                'Pressure': str(ListofData['main']['pressure']) + ' hPa',
                'Humidity': str(ListofData['main']['humidity']) + '%',
                }
        else:
            context = {'error': 'API key not found. Please check your configuration.'}
    else:
        context = {}

    return render(request, "index.html", context)
