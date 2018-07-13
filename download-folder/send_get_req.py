#This script gets the URL of Github from TestRail
import urllib.request
from testrail import * 
from get_creds import *

#Sending GET request to get the case details
client = APIClient('https://cloudbyte.testrail.com')
client.user = credentials()[0]
client.password = credentials()[1]

#Getting the github URl from test preconditions
def case_precons():
  case = client.send_get('get_case/166306')
  precons=case['custom_preconds'].split(': ')[1]
  print('precons: ',precons)
  return precons


#If precons contains URL for a specific file, use: urllib.request.urlretrieve(precons,'QWE.txt')

