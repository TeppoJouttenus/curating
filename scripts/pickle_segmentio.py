# this script analyzes segment.io logfiles

# -*- coding: utf-8 -*-
import os
import re
import json
import cPickle as pickle

# set up regexs

reTrue = re.compile(r'(?<=":)true')
reFalse = re.compile(r'(?<=":)false')
reNull = re.compile(r'(?<=":)null')

# Process data
eventFilePath = '/Volumes/Analytics/Segment.io-logs/Unpacked'
eventFiles = os.listdir(eventFilePath)
eventsAsJson = []
eventsAsString = ""

for f in eventFiles:
    with open(eventFilePath+'/'+f) as f:
        eventLines = f.readlines()
        for i in range(len(eventLines)): # clean up segment.io notation to cleaner JSON
            eventLines[i] = eventLines[i].replace('&', '&amp;')
            eventLines[i] = reNull.sub(r'"None"', eventLines[i])
            eventLines[i] = reTrue.sub(r'"True"', eventLines[i])
            eventLines[i] = reFalse.sub(r'"False"', eventLines[i])
            eventLines[i] = eventLines[i].replace('\\\"', '&quot;')
            eventsAsString += ', ' + eventLines[i]
            eventsAsJson.append(json.loads(eventLines[i]))

eventsAsString = '['+eventsAsString[1:]+']'

pickle.dump(eventsAsJson, open("/Volumes/Analytics/Segment.io-logs/eventsAsJson.p", "wb"))

with open("/Volumes/Analytics/Segment.io-logs/eventsAsString.json", 'w+') as f:
    f.write(eventsAsString)
