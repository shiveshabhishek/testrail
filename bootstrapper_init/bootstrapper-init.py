#This file take args : username, password, suite id(s) AND stores them in a file in specified PATH

import os
import datetime
import sys
import json
#suites=[798,801,804,802]


now = datetime.datetime.now()
date=str(now)[:10]
path = '/tmp/'+date+'/'

user=sys.argv[1]
password=sys.argv[2]

suite_ids=sys.argv[3:]

suite_ids=str(suite_ids)
suite_ids=suite_ids[2:-2]
print(suite_ids)


#define access rights
access_rights = 0o755

try:
  os.mkdir(path,access_rights)
except OSError:
  print("Directory %s creation failed\n" %path)
else:
  print("Successfully Created file %s \n" %path)

testrail_path=path+'testrail'

try:
  os.mkdir(testrail_path,access_rights)
except OSError:
  print("Testrail DIR creation failed(file already exists) \n")
else:
  print("Successfully Created file %s \n" %testrail_path)

suites=open(testrail_path+'/testsuites.json','w+')

if suites.write('{"username" : "' +user+ '",\n"password" : "' +password+ '", \n"suite_ids" : "'+suite_ids+'"\n}'):
  print ("Success in writing suites")
suites.close()
