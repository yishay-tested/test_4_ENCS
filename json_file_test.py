import json

with open("file.json",'r') as f:
        python_obj = json.load(f)
        print(python_obj['text'])

