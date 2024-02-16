import os
import json
from coinbase.websocket import WSClient

CONF_FILE_PATH = "conf/coinbase_cloud_api_key.json"

def load_configuration():
    if not os.path.isfile(CONF_FILE_PATH):
        return {}
    
    with open(CONF_FILE_PATH) as conf_file:
        conf = json.load(conf_file)

        return {
            "api_key": conf["name"],
            "api_secret": conf["privateKey"],
        }

if __name__ == "__main__":
    conf = load_configuration()
    if not conf:
        print("Error: Could not find the configuration file (coinbase_cloud_api_key.json) under the 'conf' folder. Did you read the README?")
        exit()

    last_message = None
    
    def on_message(message):
        global last_message
        last_message = message
        print(message)
    
    client = WSClient(api_key=conf["api_key"], api_secret=conf["api_secret"], on_message=on_message)
    client.open()
    client.subscribe(["BTC-USD"], ["heartbeats", "ticker"])
    client.sleep_with_exception_check(10)

    print(f"This is the last message received: {last_message}")
