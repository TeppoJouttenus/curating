# this script analyzes segment.io logfiles

# -*- coding: utf-8 -*-
import os
from pprint import pprint

eventFilePath = '/Volumes/Analytics/Segment.io-logs/Unpacked'
eventFiles = os.listdir(eventFilePath)
print eventFiles[0]

event1 = {"anonymousId":"4917fc78-4a0d-4ebc-830f-d2eeaa88e26f","category":None,"context":{"library":{"name":"analytics.js","version":"2.9.1"},"page":{"path":"/","referrer":"","search":"","title":"Outlearn","url":"https://pilot.outlearn.com/"},"userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36","ip":"104.129.66.226"},"integrations":{},"messageId":"4faadf53-2a75-479f-b235-9ba5615b6965","name":"index","properties":{"name":"index","path":"/","referrer":"","search":"","title":"Outlearn","url":"https://pilot.outlearn.com/"},"receivedAt":"2015-06-15T14:14:42.742Z","sentAt":"2015-06-15T14:14:42.405Z","timestamp":"2015-06-15T14:14:42.736Z","type":"page","userId":"34","channel":"client","originalTimestamp":"2015-06-15T14:14:42.399Z","projectId":"vN1tlA10Su","version":2}

event2 = {"anonymousId":"3ebb2deb-2f9d-4731-a49d-322f7fdfe169","category":None,"context":{"library":{"name":"analytics.js","version":"2.9.1"},"page":{"path":"/","referrer":"","search":"","title":"Outlearn -- My Learning","url":"https://pilot.outlearn.com/"},"userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36","ip":"146.115.44.94"},"integrations":{},"messageId":"7b2c5c2c-898b-4619-8d91-59b5ede7560d","name":"index","properties":{"name":"index","path":"/","referrer":"","search":"","title":"Outlearn -- My Learning","url":"https://pilot.outlearn.com/"},"receivedAt":"2015-06-15T15:06:13.682Z","sentAt":"2015-06-15T15:06:13.893Z","timestamp":"2015-06-15T15:06:13.679Z","type":"page","userId":"26","channel":"client","originalTimestamp":"2015-06-15T15:06:13.890Z","projectId":"vN1tlA10Su","version":2}
event3 = {"anonymousId":"3ebb2deb-2f9d-4731-a49d-322f7fdfe169","category":None,"context":{"library":{"name":"analytics.js","version":"2.9.1"},"page":{"path":"/","referrer":"","search":"","title":"Outlearn","url":"https://pilot.outlearn.com/"},"userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36","ip":"146.115.44.94"},"integrations":{},"messageId":"8a1ac2cd-3f7e-41e1-b8f2-622c729b98c9","name":"index","properties":{"name":"index","path":"/","referrer":"","search":"","title":"Outlearn","url":"https://pilot.outlearn.com/"},"receivedAt":"2015-06-15T15:06:15.678Z","sentAt":"2015-06-15T15:06:15.826Z","timestamp":"2015-06-15T15:06:15.677Z","type":"page","userId":"26","channel":"client","originalTimestamp":"2015-06-15T15:06:15.825Z","projectId":"vN1tlA10Su","version":2}



# pprint(event3)
