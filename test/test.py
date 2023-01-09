import requests

resp = requests.post("https://ml-cblnbu253a-uc.a.run.app/", files={'file': open('three.png', 'rb')})

print(resp.json())
