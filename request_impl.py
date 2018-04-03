import requests
# this is my registered api key for google maps I recieved from Google
apiKey = "AIzaSyBdHvCMgUN-3Oy7HdkzW3AguKBDpuodSYw"
url = "https://maps.googleapis.com/maps/api/geocode/json"
location = input("Entery city of address: \n")
params = {'address':location, 'key':apiKey}
r = requests.get(url =url, params = params)
data = r.json()

if data['status'] == 'OK':
    place_id = data['results'][0]['place_id']
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']
    
    print(location,'\n')
    
    print('ID: ', place_id, '\n')
    print('Latitude: ', lat, '\n')
    print('Longitude: ', lng, '\n')
else:
    print(data['status'])