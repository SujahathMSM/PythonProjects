import requests

query_char = 'sujahath@123'
url = f'https://api.pwnedpasswords.com/range/{query_char}'

res = requests.get(url)
print(res)