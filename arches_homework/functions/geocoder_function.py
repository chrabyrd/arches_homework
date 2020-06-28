from urllib.parse import quote

from arches.app.functions.base import BaseFunction

from arches_homework.tasks import _get_location_data


ADDRESS_OR_LOCATION = "Address or Location"
GEOMETRY = "Geometry"

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
    homework_model_nodes = tile.resourceinstance.graph.node_set

    location_node_uuid = homework_model_nodes.get(name=ADDRESS_OR_LOCATION).pk
    location_input_value = tile.data[str(location_node_uuid)]

    location_data_promise = _get_location_data.delay(
      quote(location_input_value)  # quote formats user input to be url-safe
    )

    geometry_node_uuid = homework_model_nodes.get(name=GEOMETRY).pk
    
    tile.data[str(geometry_node_uuid)] = location_data_promise.get()

  def post_save(self, tile, request):
    print("running after tile save")

  def on_import(self, tile, request):
    print("calling on import")

  def get(self, tile, request):
    print("calling get")

  def delete(self, tile, request):
    print("calling delete")

