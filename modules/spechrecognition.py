import json
import os
from pathlib import Path

BASE_DIR  = Path(__file__).parent.parent


with open(os.path.join(BASE_DIR,"files\speech.json"),"r") as f:
    json = json.load(f)
    json = json



def wake(inp):
    for i in range(len(json["wake"][0]["patterns"])):
        if inp == json["wake"][0]["patterns"][i]:
            return True
 

def sleep(inp):
    for i in range(len(json["sleep"][0]["patterns"])):
        if inp == json["sleep"][0]["patterns"][i]:
            return True
