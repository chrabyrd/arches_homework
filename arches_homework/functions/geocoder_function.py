import uuid
from arches.app.functions.base import BaseFunction
from arches.app.models import models
from arches.app.models.tile import Tile
import json

details = {
    "name": "Geocoder Function",
    "type": "node",
    "description": "Takes a string value from one node, geocodes it and saves it to another node",
    "defaultconfig": {"triggering_nodegroups": []},
    "classname": "GeocoderFunction",
    "component": "views/components/functions/geocoder-function",
    "functionid": "019d49c4-3d48-43c7-87e0-c84542255353",
}


class GeocoderFunction(BaseFunction):
    def save(self, tile, request):
        print("running before tile save")

    def post_save(self, tile, request):
        print("running after tile save")

    def on_import(self, tile, request):
        print("calling on import")

    def get(self, tile, request):
        print("calling get")

    def delete(self, tile, request):
        print("calling delete")
