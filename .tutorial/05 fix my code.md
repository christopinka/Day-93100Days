# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
import requests, json
from requests.auth import HTTPBasicAuth

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)
accessToken = response.json()["access_token"]

arist = input("Artist: ").lower()
artist = artist.replace(" ", "%20")

url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}
search = f"?=artist%3A{artist}&type=track&limit=5"

fullURL = f"{url}{search}"

response = requests.get(fullURL, headers=headers)
print(json.dumps(data, indent=2))  

for track in data["tracks"]["items"]:
  print(track["name"])
  print(track["preview_url"])
```
<details> <summary> 👀 Answer </summary>

```python
import requests, json, os # Missing import
from requests.auth import HTTPBasicAuth

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)
accessToken = response.json()["access_token"]

artist = input("Artist: ").lower() # Variable identifier typo
artist = artist.replace(" ", "%20")

url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}
search = f"?q=artist%3A{artist}&type=track&limit=5" # Missing 'q' in the URL - yes, this will break the code! Any incorrect URL will

fullURL = f"{url}{search}"

response = requests.get(fullURL, headers=headers)
print(json.dumps(data, indent=2))  

for track in data["tracks"]["items"]:
  print(track["name"])
  print(track["preview_url"])
```
</details>