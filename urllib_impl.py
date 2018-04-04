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

# Checks to make sure the response data is good
if json['status'] == 'OK':
    # grabs the place id
    place_id = json['results'][0]['place_id']
    # grabs the latitude value
    lat = json['results'][0]['geometry']['location']['lat']
    # and grabs the longitude value
    lng = json['results'][0]['geometry']['location']['lng']
    
    # Now print out the expected output
    print(search,'\n')
    print('ID: ', place_id, '\n')
    print('Latitude: ', lat, '\n')
    print('Longitude: ', lng, '\n')
else:
    # Print out the status if the response data was not OK
    print(json['status'])
