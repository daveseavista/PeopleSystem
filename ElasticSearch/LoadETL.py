__author__ = 'dave'

import json
from datetime import datetime
from elasticsearch import Elasticsearch

json_data=open("/home/dave/play.json").read()
data = json.loads(json_data)

es = Elasticsearch()


id_val =0

for i in data:
    for doc in data[i]:
        res = es.index(index="etl", doc_type='run_summary', id=id_val, body=doc)
        id_val = id_val+1

#print(res['created'])


