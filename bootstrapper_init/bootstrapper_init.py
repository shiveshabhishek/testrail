#This file take args : Build number, suite id(s) AND stores them in a file in specified PATH
import os
import datetime
import sys
import argparse

#Fetch Date
now = datetime.datetime.now()
date=str(now)[:10]

#Get arguments from command line
parser = argparse.ArgumentParser(description='Bootstrapper init to create directories and file containing list of suites')
parser.add_argument('-bn', '--build_number', help='Build number from Jenkins', required=True)
parser.add_argument('-sid', '--suite_ids', help='Suite IDs to be added to the Plan', required=True)
args = vars(parser.parse_args())
build_number=args['build_number']
suite_ids=args['suite_ids']

path='/tmp/'+date+'-'+build_number+'/'
#define access rights
access_rights = 0o755

#Create file in specified directory
testrail_path=path+'testrail'
try:
  os.makedirs(testrail_path,access_rights)
except OSError:
  print("Testrail DIR creation failed(file already exists) \n")
else:
  print("Successfully Created file %s \n" %testrail_path)
#Open and write file to the newly created directory
suites_file=open(testrail_path+'/testsuites.json','w+')
if suites_file.write('{\n  "build_number" : "' +build_number+ '", \n  "suite_ids" : "'+suite_ids+'"\n}'):
  print ("Success in writing suites to file")
else:
  print('Error writing suites to file')
suites_file.close()
