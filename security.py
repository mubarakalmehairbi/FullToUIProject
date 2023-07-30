"""
This script creates a function that validates the WebSocket connection (ws) and the data sent to the server
via WebSockets. In order to understand them, check these two links:
- https://toui.readthedocs.io/en/latest/toui.apps.Website.set_ws_validation.html
- https://toui.readthedocs.io/en/latest/toui.apps.Website.set_data_validation.html

These security measures are not perfect. Modify these functions to add your own security measures. And do not forget
to change `only_valid_domains` to True.
"""
import json

# Change this to a list of domains that are allowed to send data to your app via WebSockets.
only_valid_domains = False # Change this to True later. Otherwise, connections from non-valid domains will be accepted.
valid_domains = []

def ws_validation(ws: "simple_websocket.ws.Server"):
    # The environ dict might contain relevant data when valodating a WebSocket connections. Trying printing it to explore it.
    #print(ws.environ)
    if only_valid_domains:
        # Check if the connection is coming from a valid domain.
        if ws.environ.get("HTTP_ORIGIN") not in valid_domains:
            return False
    return True

def data_validation(data):
    # The data sent to the server via WebSockets is a JSON string. You can convert it to a Python dict using the json module.
    data_dict = json.loads(data)
    # Check if the dictionary contains an unknown key. Note that the keys in ToUI might change later on, so it might be helpful to
    # check the types of keys that ToUI receives in this URL: https://toui.readthedocs.io/en/latest/how_it_works.html#instructions-sent-and-received.
    known_keys = ["type", "func", "args", "selector-to-element", "url", "html", "uid", "selector", "files", "msg-num", "name", "size",
                  "file-type", "last-modified", "file-id", "data", "end"]
    for key in data_dict.keys():
        if key not in known_keys:
            return False
    return True