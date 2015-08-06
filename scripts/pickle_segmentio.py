# this script analyzes segment.io logfiles

# -*- coding: utf-8 -*-
import os
import json
import cPickle as pickle

# Process data
eventFilePath = '/Volumes/Analytics/Segment.io-logs/Unpacked'
eventFiles = os.listdir(eventFilePath)
events = []

for f in eventFiles:
    with open(eventFilePath+'/'+f) as f:
        eventLines = f.readlines()
        for i in range(len(eventLines)):
            eventLines[i] = eventLines[i].replace('null', '\"None\"')
            events.append(json.loads(eventLines[i]))

pickle.dump(events, open("/Volumes/Analytics/Segment.io-logs/events_test.p", "wb"))
