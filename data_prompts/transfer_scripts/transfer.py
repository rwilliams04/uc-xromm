#!/usr/bin/env python 
"""

Template script that prompts the user for trial metadata and outputs
`metadatafile.json`. This file is then transferred to a specified 
endpoint via Globus using their python transfer client library.

"""
import re
import os
import sys
import json
import datetime
from collections import defaultdict as dd
from apscheduler.schedulers.blocking import BlockingScheduler
from globusonline.transfer import api_client
from globusonline.transfer.api_client import Transfer
from globusonline.transfer.api_client.goauth import get_access_token


# Get Globus nexus access token. Prompts for username and password
auth = get_access_token()

def autodict():
    return dd(autodict)

d = autodict()

def prompt_for(question, options=[], regex=''):
    if options:
        print question, "\n"
        for (i, opt) in enumerate(options):
            print("\t{} - {}".format(i, opt))
        print
        resp = int(raw_input('>>> '))
        if 0 <= resp < len(options):
            return options[resp]
        return prompt_for(question, options, regex)
    resp = raw_input(question + ' >>> ')
    if regex:
        rgx = re.compile(regex)
        if rgx.match(resp):
            return resp
        print("Invalid input")
        return prompt_for(question, regex=regex)
    return resp

d['firstname'] = prompt_for("first name? (max 50 chars)", regex=r'\w[a-z_ ]+')
d['lastname'] = prompt_for("last name? (max 50 chars)", regex=r'\w[a-z_ ]+')
d['date'] = prompt_for("date? (YYYY/MM/DD)", regex=r'\d{4}/\d{2}/\d{2}')

fname = "data.json"
base_path = os.getcwd()
file_path = base_path + fname
dest_path = "/~/" + fname

f = open(file_path, 'w')
f.write(json.dumps(d))
f.close()


### TRANSFER SETUP ###

src = "rwilliams#rwilliams01"     # source endpoint
dst = "jvoigt#midway-transfers"   # destination endpoint

# authenticate using access token
api = api_client.TransferAPIClient(
    username=auth.username, 
    goauth=auth.token
)

# activate endpoints
status, message, data = api.endpoint_autoactivate(src)
status, message, data = api.endpoint_autoactivate(dst)

# get submission id
code, reason, result = api.transfer_submission_id()
submission_id = result["value"]

# designate endpoints(1) and items(2) for transfer(3)
def transfer(id, source, dest):
	t = Transfer(id, source, dest)
	t.add_item(file_path, dest_path)
	status, reason, result = api.transfer(t)
	os._exit(1)


### SCHEDULE TRANSFER JOB ###

scheduler = BlockingScheduler()
now = datetime.datetime.now()

scheduler.add_job(lambda: 
    transfer(submission_id, src, dst), 
    'date', 
    run_date=datetime.datetime(now.year, now.month, now.day, 23, 59, 0)
)

# returns 0 in the child, pid of the child in the parent
if os.fork(): 
    sys.exit()

scheduler.start()
