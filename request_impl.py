# this library works best on linux running python2.*
import requests
# this is my registered api key for google maps I recieved from Google
apiKey = "AIzaSyBdHvCMgUN-3Oy7HdkzW3AguKBDpuodSYw"
# the base url endpoint to retreive our json data from
url = "https://maps.googleapis.com/maps/api/geocode/json"
#asks the user to enter an address or city
location = input("Entery an address or city: \n")
# in this step, we would the parameters that we need to add to our base endpoint
params = {'address':location, 'key':apiKey}
# in this step we make restful api get call using the the requests 
# library and also the url and parameters we built above
response = requests.get(url =url, params = params)
# next we take our response to that the restful api call and extract the json data from it
data = response.json()

# next we take a look at the status of this json
# if the status is OK then we proceed.
if data['status'] == 'OK':
    # in these next few lines we extract the information we need from the json object
    place_id = data['results'][0]['place_id']
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']
    
    # next we simply print this information.
    print(location,'\n')
    print('ID: ', place_id, '\n')
    print('Latitude: ', lat, '\n')
    print('Longitude: ', lng, '\n')
else:
    # if the status was not OK, then we simply print out the status of the response.
    print(data['status'])