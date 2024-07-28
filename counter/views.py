import requests
import json
from django.shortcuts import render
#b7Cnje/Z6lNVTwAASB3AqA==JdSnfu3IT2BzsgtA
# Creating a view for the home page
def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.edamam.com/api/nutrition-data?'
        app_id = 'app_id=38315c1f&'
        app_key = 'app_key=5cdf0bd788402df68533c8826e56b22b	'
        api_request = requests.get(api_url + app_id + app_key + '&nutrition-type=logging&ingr=' + query)
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "oops! something went wrong"
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a food item to get its nutrition details'})
