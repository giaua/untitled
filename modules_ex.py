import requests
r = requests.get('http://example.com') # Простой GET запрос
print(r.text) # vuvod otveta servera


url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par)   # Transfer parameters into query
print(r.url)    # Created url-adress with paremeters par

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)  # sending cookie to server
print(r.text)

print(r.cookies['example_cookie_name']) # using cookies, recaived from the server