# this script analyzes segment.io logfiles

# -*- coding: utf-8 -*-
import os
import json
import sys
import zorba_api
import cPickle as pickle
from pprint import pprint

# load data
events = pickle.load(open("/Volumes/Analytics/Segment.io-logs/events_test.p", "rb"))

# print json.dumps(events[1])
# pprint(events[0])

# load zorba
store = zorba_api.InMemoryStore_getInstance()
zorba = zorba_api.Zorba_getInstance(store)

# create zorba query
eventString = json.dumps(events[0])
for i in range(1,40):
    eventString += ', '+json.dumps(events[i])

query = '''let $events := [''' + eventString + \
''']
let $join :=
  for $event in jn:members($events)
  where $event("event") = "Entered Section"
  return {
    "userID" : $event("userId"),
    "Path Title" : $event("properties")("Path Title"),
    "Module Title" : $event("properties")("Module Title"),
    "Section Title" : $event("properties")("Section Title")
  }
return [$join]
'''


# run zorba query
xquery = zorba.compileQuery(query)
# print xquery.execute()
pprint(json.loads(xquery.execute()))

# shut down zorba, free up memory
xquery = None
zorba.shutdown()
zorba_api.InMemoryStore_shutdown(store)
