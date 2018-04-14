import requests
import os
import re

data_folder = os.path.join(os.getcwd(), 'data')


for each_file in os.listdir(data_folder):
    m = re.match('(players)(\d*)(\\.json_jsonld)', each_file)
    if m:
        with open(data_folder+'/'+each_file, 'r') as c_f:
            content = c_f.read()
            print(content)
            req_url = "http://rdf-translator.appspot.com/convert/json-ld/nt/content="+content
            r = requests.post(req_url)
            print(r.url)
            print(r.text)
            input()
