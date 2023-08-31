"""
     Homepage: yelp.com/developers/v3/manage_app

     Fist we make an account and then register an app in yelp website.
     then it give an api key which is secret for user
"""
import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers={
     "Authorization": "Bearer " + config.api_key
}
params = {
     "term":"Barber",
     "location":"NYC"
}
response = requests.get(url, headers=headers,params=params)
businessess = response.json()["businesses"]

names=[business["name"] for business in businessess if business["rating"] > 4.5 ]
print(names)