#!/usr/bin/env python 

import os
import sys
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

logging.basicConfig()
now = datetime.datetime.now()
when = datetime.datetime(now.year, now.month, now.day, 16, 30, 0)

def hi():
    print "hi!"
    os._exit(1)
    

runner = BlockingScheduler()
runner.add_job(hi, 'date', run_date=when)

# returns 0 in the child, pid of the child in the parent
if os.fork(): sys.exit()

runner.start()
