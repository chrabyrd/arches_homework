from __future__ import absolute_import, unicode_literals

from arches_homework.celery import app
import requests

@app.task
def _foo():
  response = requests.get(
    'https://api.mapbox.com/geocoding/v5/mapbox.places/Los%20Angeles.json', 
    params={'access_token': 'pk.eyJ1IjoiY2hpYXR0IiwiYSI6ImZRLTZDbVkifQ.2ZLLC1kInvxJ7isk_0_OMw'}
  )

  return response.json()