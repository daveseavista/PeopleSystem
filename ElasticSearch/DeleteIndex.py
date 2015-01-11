__author__ = 'dave'


from elasticsearch import Elasticsearch

es = Elasticsearch()

noOfRows = es.count(index=['etl2'],doc_type=['run_summary2'])

MaxRows = noOfRows['count']

print(MaxRows)

for x in range(0,MaxRows):
    rs = es.delete(index=['etl2'],doc_type=['run_summary2'],id=[str(x)])