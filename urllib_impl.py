import json as JSON
import urllib

# this is my registered api key for google maps I recieved from Google
apiKey = "AIzaSyBdHvCMgUN-3Oy7HdkzW3AguKBDpuodSYw"

def urlQuery(city):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="
    elements = city.split(' ')
    for element in elements:
        url += '+' + element
    url += ",+USA&key=" + apiKey
    return url

#have the user enter in the city they want to search
#store what they enter into the variable 'city'
search = input("Enter a city or address to search: \n")

# calls the urlQuery function and passes the user input, 'search', to get the build query url. 
url = urlQuery(search)
# Uses the urllib library to make a get request on 'url'
req = urllib.request.Request(url)
# this opens that request and retieves the response
response = urllib.request.urlopen(req)
# now turn this response into a json object using the json library
json = JSON.loads(response.read())

## First Issue I ran into ##
# ran into issues with the geocoder returning weird latitude and longitude cordinates 
# this occured when you only search for a city and not a full address
# work around for this that I found was to change the 'key' parameter in the url from '+CA&key=' to '+USA&key='
# this puts the searched city or address in the reference of the whole USA instead of just California


if json['status'] == 'OK':
    place_id = json['results'][0]['place_id']
    lat = json['results'][0]['geometry']['location']['lat']
    lng = json['results'][0]['geometry']['location']['lng']
    
    print(search,'\n')
    
    print('ID: ', place_id, '\n')
    print('Latitude: ', lat, '\n')
    print('Longitude: ', lng, '\n')
else:
    print(json['status'])

## Second Issue I ran into ##
# when trying to extract the place id, latitude, and longitude from the recieved json data,
# I was trying to get it by doing json['results']['place_id'],
# however, I did not realize that the 'results' object within the json was an array
# the solution for this is to instead extract it  by doing json['results'][0]['place_id']
# which grabs the first index of results, which seems to be the important index with all the information in it.