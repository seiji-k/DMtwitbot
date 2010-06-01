#!/usr/bin/python
# -*- coding: utf-8 -*-

# Using python-twitter; a python wrapper around the Twitter API
# (http://code.google.com/p/python-twitter/)
#and bsddb
#(http://pybsddb.sourceforge.net/)

import twitter
import re
from time import sleep
import bsddb
dm_log = bsddb.btopen('/tmp/dmlog.db' )
api = twitter.Api(username='********', password= '*********')

hushtug = re.compile("#test")        #Defining a hushtug


DMs = api.GetDirectMessages()   #Get a list of DMs that have never been seen. 

DMs.reverse()
for dm in DMs :
    dm_id = dm.id
    if str(dm_id) not in dm_log :              
               print dm_id
               text = dm.GetText()           # Getting a text
               print text
               try:
                       api.PostUpdate(text)                             # Posting a text
                       dm_log [ str(dm_id) ] = str(dm)
               except:
                       print "Error: Post Update error...."
               sleep(5)                                                 #  To prevent HTTP error 403

dm_log.sync
dm_log.close()





