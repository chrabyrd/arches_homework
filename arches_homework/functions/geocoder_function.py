import uuid
from arches.app.functions.base import BaseFunction
from arches.app.models import models
from arches.app.models.tile import Tile
import json


from arches_homework.tasks import _foo


details = {
    "name": "Geocoder Function",
    "type": "node",
    "description": "Takes a string value from one node, geocodes it and saves it to another node",
    "defaultconfig": {"triggering_nodegroups": []},
    "classname": "GeocoderFunction",
    "component": "views/components/functions/geocoder-function",
    "functionid": "019d49c4-3d48-43c7-87e0-c84542255353",
}

# import pdb; pdb.set_trace()

# MAPBOX API KEY pk.eyJ1IjoiY2hpYXR0IiwiYSI6ImZRLTZDbVkifQ.2ZLLC1kInvxJ7isk_0_OMw

# start the worker with -I celery.task.http

class GeocoderFunction(BaseFunction):
    def save(self, tile, request):

        bar = _foo.delay()
        baz = bar.get()

        print(baz)

    def post_save(self, tile, request):
        print("running after tile save")

    def on_import(self, tile, request):
        print("calling on import")

    def get(self, tile, request):
        print("calling get")

    def delete(self, tile, request):
        print("calling delete")

