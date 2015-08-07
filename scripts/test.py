# -*- coding: utf-8 -*-
import os
import json
import sys
import zorba_api
import cPickle as pickle
from pprint import pprint

text = '{"anonymousId": "dea2ac0c-87e0-4906-a669-cdb0751bd7b9", "projectId": "vN1tlA10Su", "messageId": "c9dd38b5-397c-4aa5-b16e-07f601a89071", "userId": "67", "integrations": {}, "properties": {"taskText": "Try parsing the string \"10.2abc\" with parseInt() and parseFloat().", "hasDeliverable": "False", "taskId": "2210"}, "receivedAt": "2015-06-16T14:20:57.434Z", "version": 2, "channel": "client", "context": {"userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36", "page": {"url": "https://pilot.outlearn.com/learn/supermegacorp/node-path/1", "path": "/learn/supermegacorp/node-path/1", "search": "", "referrer": "", "title": "Outlearn -- JavaScript Backends with Nodejs"}, "library": {"version": "2.9.1", "name": "analytics.js"}, "ip": "104.129.66.226"}, "timestamp": "2015-06-16T14:20:57.428Z", "type": "track", "event": "Checked Task", "originalTimestamp": "2015-06-16T14:20:57.366Z", "sentAt": "2015-06-16T14:20:57.372Z"}'

print repr(text.replace('\\\"', '&quot;'))

text = '{"anonymousId": "dea2ac0c-87e0-4906-a669-cdb0751bd7b9", "projectId": "vN1tlA10Su", "messageId": "c9dd38b5-397c-4aa5-b16e-07f601a89071", "userId": "67", "integrations": {}, "properties": {"taskText": "Try parsing the string \"test\" with parseInt() and parseFloat()."}}'

# j = json.loads(text)
