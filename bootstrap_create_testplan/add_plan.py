#This script needs 3 arguments: username, password, Build number 
import pprint
import os
import sys
import datetime
from testrail import * 

now=datetime.datetime.now()
date=str(now)[:10]
#suites=[798,801,804,802]
build_no=sys.argv[3]
username=sys.argv[1]
password=sys.argv[2]

path='/tmp/'+date+'/testrail/'

access_rights = 0o755

suite_file=open(path+'testsuites.json','r')

suites=suite_file.read()
suites=json.loads(suites)

# print(suites)

suite_ids=suites['suite_ids']
# print(suite_ids)

suite_id=suite_ids.split(',')
# print(suite_id)


suite_file.close()
print('suites to be added: ')

for suite in suite_id:
  print(suite)


client = APIClient('https://cloudbyte.testrail.com')
client.user = username
client.password = password

plan_name=date+'-build-'+build_no
plan = client.send_post('add_plan/3',
  {'name':plan_name ,'description': 'creating from API call'}
)


plan_id=str(plan['id'])
print('Plan created.\nPlan id:',plan_id)

for suite in suite_id:
  plan_entry=client.send_post('add_plan_entry/'+plan_id,
  {'suite_id':suite,'description': 'This Test Plan is Created via bootstrap_create_testplan'}
  )

print('------PLAN CREATED SUCCESSFULLY-----')

result_path=path+'plan-'+str(plan_name)

try:
  os.mkdir(result_path,access_rights)
except OSError:
  print("Directory %s creation failed\n" %path)
else:
  print("Successfully Created file %s \n" %path)

tp_result=open(result_path+'/result.json','w+')
if tp_result.write('{"plan_name" : "' +plan_name+ '",\n"plan_id" : "' +plan_id+ '",\n"Status" : "Plan Created(Passed)"\n}'):
  print ("Success in creating test plan result file")
else:
  print("Error creating Test Plan result file")
tp_result.close()

