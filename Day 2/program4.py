#Q4. Write a Python program using the requests module to send a GET request to a given URL API endpoint and print the JSON response

import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

print("JSON Response:", response.json())