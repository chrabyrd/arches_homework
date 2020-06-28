from __future__ import absolute_import, unicode_literals

import requests

from arches_homework.celery import app


@app.task
def _get_location_data(url_safe_location):
  response = requests.get(
    'https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json'.format(url_safe_location), 
    params={
    	'access_token': 'pk.eyJ1IjoiY2hpYXR0IiwiYSI6ImZRLTZDbVkifQ.2ZLLC1kInvxJ7isk_0_OMw',  # could use Tile.objects.db_manager() to get token, but is it graceful?
    	'limit': 1,  # since we're only using the most accurate return, let's speed up the API call
    }
  )

  return response.json()