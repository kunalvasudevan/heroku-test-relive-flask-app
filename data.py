# Importing required libraries 
from googleplaces import GooglePlaces, types
import geocoder
import requests 
import json 
  

g = geocoder.ip('me')
print(g.latlng)
my_lat_lng ={'lat': g.latlng[0], 'lng': g.latlng[1]}
  
# Use your own API key for making api request calls 
API_KEY = 'AIzaSyBr8V0XkaNFYkNXcP6eJc76b6YutvizwNw'
  
# Initialising the GooglePlaces constructor 
google_places = GooglePlaces(API_KEY) 

# storing returned data
my_places_data = {}   # dictionary

# my_places_data = {
#      '1': [place.name, place.local_phone_number]    #its a list,
#      '2': [place2.name, so on.....],
#      '3': [data]
# }


# function to return nearest hospitals data 
def generate_DATA():
    query_result = google_places.nearby_search( 
            # lat_lng ={'lat': 46.1667, 'lng': -1.15}, 
            lat_lng = my_lat_lng, 
            radius = 5000, 
            types =[types.TYPE_HOSPITAL]) 
    

    # If any attributions related  
    # with search results print them 
    if query_result.has_attributions: 
        print (query_result.html_attributions) 

    # Iterate over the search results 
    counter = 0;
    for place in query_result.places: 
        if (counter == 10): break
        counter += 1;
        place.get_details()

        my_places_data[counter] = [
            place.name,
            place.local_phone_number,
            place.international_phone_number
        ]
    # returning final data
    return my_places_data
