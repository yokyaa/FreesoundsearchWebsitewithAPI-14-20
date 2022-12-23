import requests
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')

search_input = input("Which sound you looking for?: ")
url = f"https://freesound.org/apiv2/search/text/?query={search_input}&token={API_KEY}"
response = requests.get(url)
response.raise_for_status()
data=response.json()
for result in range(len(data["results"])):
    sound_id = data["results"][result]["id"]
    sound_username = data["results"][result]["username"]
    sound_url = f"https://freesound.org/people/{sound_username}/sounds/{sound_id}/"
    print(f"Music URL : {sound_url}")
    dl_url = f"https://freesound.org/apiv2/sounds/{sound_id}/download/"
    print(f"Download URL: {url}")