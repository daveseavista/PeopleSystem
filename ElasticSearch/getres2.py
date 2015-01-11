__author__ = 'dave'

from elasticsearch import Elasticsearch

es = Elasticsearch()

rs = es.search(index=['megacorp'],
               scroll='10s',
               search_type ='scan',
               size=100,

               body={
                   'fields' :['first_name','age','intrests'],
                    'query':{
                        'match':{'last_name': 'smith'}
                    }
               }




)

scroll_id = rs['_scroll_id']

results =[]
scroll_size =rs['hits']['total']

print scroll_size

while(scroll_size >0):
    try:
        rs =es.scroll(scroll_id=scroll_id,scroll='10s')
        results += rs['hits']['hits']
        scroll_id =rs['scroll_id']
        scroll_size =len(rs['hits']['hits'])
    except:
        break

for results in results:
    print results['_id'],results['fields']['first_name'],results['fields']['age'],results['fields']['intrests']

