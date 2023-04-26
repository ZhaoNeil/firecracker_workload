import json
from urllib.request import urlopen
from time import time


def lambda_handler(link):
    # link = event['link']  # https://github.com/jdorfman/awesome-json-datasets

    start = time()
    f = urlopen(link)
    data = f.read().decode("utf-8")
    network = time() - start

    start = time()
    json_data = json.loads(data)
    str_json = json.dumps(json_data, indent=4)
    latency = time() - start

    return {"network": network, "serialization": latency}

if __name__ == "__main__":
    link = "https://blockchain.info/unconfirmed-transactions?format=json"
    result = lambda_handler(link)
    print(result)

