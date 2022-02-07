"""но есть более удобная библиотека, которая реализует в себе все методы http протокола"""

import requests

# pip install requests
# requests - уже использует у себя внутри библиотеку urlLib
response1 = requests.get('https://example.com/')
response2 = requests.put('https://example.com/')
response3 = requests.post('https://example.com/')
response4 = requests.delete('https://example.com/')
