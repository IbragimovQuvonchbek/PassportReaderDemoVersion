import requests

url = 'http://127.0.0.1:5000/process'
files = {'imagefile': open('img.png', 'rb')}

response = requests.post(url, files=files)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Failed to process the image:', response.text)
