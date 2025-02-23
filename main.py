import json
import os

import requests
from flask import Flask, request
from replit import db
from requests.auth import HTTPBasicAuth

# def create_counter(initial_value):
#   def increment():
#       nonlocal initial_value
#       initial_value += 1
#       return initial_value
yearIncrement = 0

def getYearOffset():
  
  global yearIncrement
  print(f"yearIncrement 1: {yearIncrement}")
  offset = yearIncrement
  if offset > 200:
    yearIncrement = 0
  else:
    yearIncrement += 10
  print(f"yearIncrement 2: {yearIncrement}")
  return yearIncrement



def getTracks(year):
  clientID = os.environ['CLIENT_ID']
  clientSECRET = os.environ['CLIENT_SECRET']

  url = "https://accounts.spotify.com/api/token"
  data = { "grant_type": "client_credentials"}
  auth = HTTPBasicAuth(clientID, clientSECRET)

  response = requests.post(url, data=data, auth=auth)
  accessToken = response.json()["access_token"]

  offset = getYearOffset()
  
  print(f"offset: {offset}")
  
  print(f"year: {year}")
  
  headers = {"Authorization" : f"Bearer {accessToken}"}
  url = "https://api.spotify.com/v1/search"
  search = f"?q=year%3A{year}&type=track&limit=10&offset={offset}"

  fullURL = f"{url}{search}"

  response = requests.get(fullURL, headers=headers)
  data = response.json()
  # print(json.dumps(data, indent=2))

  songs = ""
  f = open("songs.html", "r")
  songs = f.read()
  f.close()

  listSongs = ""

  for track in data["tracks"]["items"]:
    thisTrack = songs
    thisTrack = thisTrack.replace("{name}",f"""{track["name"]} by {track["artists"][0]["name"]}""")
    thisTrack = thisTrack.replace("{url}", track["preview_url"] or "No preview available")
    listSongs += thisTrack

  return listSongs

app = Flask(__name__)


@app.route("/", methods=["POST"])
def change():
  page = ""
  f = open("form.html", "r")
  page = f.read()
  f.close()
  year = request.form["year"]
  songs = getTracks(year)
  page = page.replace("{songs}",songs)
  page = page.replace("{value}",year)
  return page


@app.route('/')
def index():
  page = ""
  f = open("form.html")
  page = f.read()
  f.close()
  page = page.replace("{songs}","")
  page = page.replace("{value}","1990")
  return page


app.run(host='0.0.0.0', port=81)
