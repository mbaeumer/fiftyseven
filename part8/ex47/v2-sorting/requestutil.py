import urllib.request
import urllib.parse
import json

def get_raw_data(url):
  f = urllib.request.urlopen(url)
  return json.loads(f.read().decode('utf-8'))
