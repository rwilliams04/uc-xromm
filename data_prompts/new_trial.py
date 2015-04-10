#!/usr/bin/env python 
"""
A little script that prompts the user for trial metadata and outputs
`trial.json`.

"""
import re
import json
from collections import defaultdict as dd

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


d['type'] = prompt_for("trial type?", ["regular trial", "calibration file"])
d['name'] = prompt_for("trial name? (max 50 chars)", regex=r'\w[a-z_ ]+')
d['date'] = prompt_for("trial date? (YYYY/MM/DD)", regex=r'\d{4}/\d{2}/\d{2}')

more_info = prompt_for("do you have subject info to enter? (y|n)", 
                       regex=r'[yn]$') 

if more_info is "y":
    print "prompt for more stuff"

print(json.dumps(d))
