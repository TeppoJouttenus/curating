# this script analyzes segment.io logfiles

# -*- coding: utf-8 -*-
import os
import json
import sys
import zorba_api
import cPickle as pickle
from pprint import pprint

def runZorba(query):
    # load zorba
    store = zorba_api.InMemoryStore_getInstance()
    zorba = zorba_api.Zorba_getInstance(store)

    # run zorba
    xquery = zorba.compileQuery(query)
    output = xquery.execute()

    # shut down zorba, free up memory
    xquery = None
    zorba.shutdown()
    zorba_api.InMemoryStore_shutdown(store)

    return output

def createEnteredSectionQuery(eventString, sectionName):
    query = '''let $events := ''' + eventString + \
    '''
    let $join :=
      for $event in jn:members($events)
      where $event("event") = "Entered Section"
      where $event("properties")("Path Title") = "JavaScript Backends with Node.js"
      where $event("properties")("Module Title") = "A re-introduction to JavaScript (JS tutorial)"
      where $event("properties")("Section Title") = "'''+sectionName+'''"
      return {
        "userID" : $event("userId"),
        "Path Title" : $event("properties")("Path Title"),
        "Module Title" : $event("properties")("Module Title"),
        "Section Title" : $event("properties")("Section Title")
      }
    return [$join]
    '''
    return query

# load data as JSON
events = pickle.load(open("/Volumes/Analytics/Segment.io-logs/eventsAsJson.p", "rb"))

# load data as string
with open("/Volumes/Analytics/Segment.io-logs/eventsAsString.json", ) as f:
    eventString = f.read()

pprint(events[3])

# # old way
# eventString2 = json.dumps(events[0])
# for i in range(1,len(events)):
#     eventString2 += ', '+json.dumps(events[i])
# eventString2 = '['+eventString2+']'



# run zorba query
query = createEnteredSectionQuery(eventString, "Introduction")
queryResult = json.loads(runZorba(query))
pprint(queryResult)
print len(queryResult)
query = createEnteredSectionQuery(eventString, "Overview")
queryResult = json.loads(runZorba(query))
pprint(queryResult)
print len(queryResult)
query = createEnteredSectionQuery(eventString, "Numbers")
queryResult = json.loads(runZorba(query))
pprint(queryResult)
print len(queryResult)
query = createEnteredSectionQuery(eventString, "Strings")
queryResult = json.loads(runZorba(query))
pprint(queryResult)
print len(queryResult)
query = createEnteredSectionQuery(eventString, "Other types")
queryResult = json.loads(runZorba(query))
pprint(queryResult)
print len(queryResult)
