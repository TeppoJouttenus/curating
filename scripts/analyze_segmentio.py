# this script analyzes segment.io logfiles

# -*- coding: utf-8 -*-
import os
import json
from pprint import pprint

eventFilePath = '/Volumes/Analytics/Segment.io-logs/Unpacked'
eventFiles = os.listdir(eventFilePath)
events = []

for f in eventFiles:
    with open(eventFilePath+'/'+f) as f:
        eventLines = f.readlines()
        for i in range(len(eventLines)):
            eventLines[i] = eventLines[i].replace('null', '\"None\"')
            events.append(json.loads(eventLines[i]))

for i in range(3):
    pprint(events[i])
