from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def home(request):
    title = "Home"
    data = {"title" : title}

    if request.method == "POST":
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+"&appid=7034f3ae944485140437e804cf6429ed").read()         
  
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "title" : "Home"
        }
    else:
        data = {"title" : title}    


    return render(request , 'main/index.html' , data)