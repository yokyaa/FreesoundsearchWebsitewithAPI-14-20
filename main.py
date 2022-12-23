# Search free sound website with flask and HTTP request api
from flask import Flask, request,render_template,send_from_directory
import urllib.request
import requests
import os
import dotenv
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv('API_KEY')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search',methods=['POST'])
def search():
    query = request.form['query']
    url = f"https://freesound.org/apiv2/search/text/?query={query}&token={API_KEY}"
    response = requests.get(url)
    data = response.json()
    results = data['results']
    for result in results:
        result['url'] = f"https://freesound.org/people/{result['username']}/sounds/{result['id']}/"

        download_url = f"https://freesound.org/apiv2/sounds/{result['id']}/download/"

        result['download_url'] = download_url
        save = requests.get(download_url)
        print(save.status_code)
        if save.status_code == 200:
            with open(f'/static/sounds/{result["name"]}.mp3', 'wb') as f:
                f.write(response.content)
        return send_from_directory('/static/sounds', f'{result["name"]}', mimetype='audio/mpeg')

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
