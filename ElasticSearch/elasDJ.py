__author__ = 'dave'

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
    'first_name': 'John',
    'last_name': 'Smith',
    'age':  25,
    'about': 'I love rock climbing',
    'intrests': ['sports', 'music']
}


res = es.index(index="megacorp", doc_type='employee', id=1, body=doc)
print(res['created'])

