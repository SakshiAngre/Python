import requests

r=requests.get('https://api.spotify.com/')

with open("Spotify.txt","w") as f:
    f.write(r.text)