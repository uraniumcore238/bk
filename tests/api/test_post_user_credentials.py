import requests

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '1028263814841499708'
CLIENT_SECRET = '9wetGpv-udhq8qGU03Vu-yuVHEOkvdzt'
REDIRECT_URI = 'https://nicememe.website'


def test_exchange_code():
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': 'MzgwNDI4ODYyMzM0Njk3NDcz.GJI_rl.JbyrbQGaQQ7F_gwFio8HAoCkI2aty-LZ8xCaEI',
    'redirect_uri': REDIRECT_URI
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
  r.raise_for_status()
  print(r.json())
  return r.json()
