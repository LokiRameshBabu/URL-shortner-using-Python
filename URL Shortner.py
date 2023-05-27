import requests
def shorten_url(long_url):
    access_token = '606b279751344959acf9916938eb701d4b3c6245'
    api_url = f'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',}
    payload = {
        'long_url': long_url,}
    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        short_url = data.get('id')
        return short_url
    else:
        print(f'Failed to shorten URL: {response.content}')
long_url = 'https://example.com/very-long-url'
short_url = shorten_url(long_url)
print(f'Shortened URL: {short_url}')