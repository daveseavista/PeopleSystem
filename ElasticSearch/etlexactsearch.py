__author__ = 'dave'

from elasticsearch import Elasticsearch

es = Elasticsearch()

rs = es.search(index=['etl2'],
               scroll='10s',
               search_type ='scan',
               size=100,

               body={
#                   'fields': ['MODULE_NAME', 'DWH_START_DATE', 'DATAFLOW_NAME', '_id','childData.MODULE_RUN_SK'],
                    'query':{
                        'match_all': {}
#                        'match':{'_id': '262'}
#                       'match':{'MODULE_NAME': 'clean_clos_title'}

                    }
               }
)

scroll_id = rs['_scroll_id']

results =[]
scroll_size =rs['hits']['total']

#print "scroll size "  + str(scroll_size)

while(scroll_size >0):
    try:
        rs =es.scroll(scroll_id=scroll_id,scroll='10s')
        results += rs['hits']['hits']
        scroll_id =rs['scroll_id']
        scroll_size =len(rs['hits']['hits'])
    except:
        break

#print results

for results in results:
#    print results['_id'],results['fields']['MODULE_NAME'],results['fields']['START_DATE'],results['fields']['ROWS_WRITTEN']
#   print results['fields']['childData.MODULE_RUN_SK']
    print results