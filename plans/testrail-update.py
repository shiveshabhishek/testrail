#Single File to create a plan inside a project,add suites and update cases(from csv file)
# to a newly created run within that plan

from testrail import * 
import pprint
import csv

#Setting up credentials and URL
client = APIClient('https://cloudbyte.testrail.com')
client.user = '------'
client.password = '------'

#Creating Plan inside project
plan= client.send_post(
    'add_plan/3',
    { 'name': 'TESTPLAN', 'description': 'Making plan from API call'}
)

#Getting Plan ID
planid=plan['id']

#Fetching Suite_id,Case_id and Result from CSV file
suite_ids=[]
case_ids=[]
results=[]
csvfile = csv.reader(open('log.csv','r'))
for row in csvfile:
  suite_id=row[2].split(':')[1]
  suite_ids.append(suite_id)

  case_id=row[1].split(':')[1]
  case_ids.append(case_id)
  
  result=row[3].split(':')[1]
  if str(result)=='Passed':
      result=1
  else:
      result=5
  results.append(result)
  
#Getting the number of entries
size=len(suite_ids)

print('Size=',size)

#Printing Unique Suite_ids
print(set(suite_ids))  

#Adding entries to plan
for suites in set(suite_ids):
  plan_entry=client.send_post(
      'add_plan_entry/'+str(planid) ,
      {'suite_id': suites, 'description': 'Testing for creation via API'}
  )
  #Fetching Run_id from plan_entries
  run_id= plan_entry['runs'][0]['id']
  print('Run id:', run_id)
  i=0
  #Adding Cases and results For each unique Suite_id inside respective Run
  while i<size:
    if(suites==suite_ids[i]):
      add_result=client.send_post(
       'add_result_for_case/'+str(run_id)+'/'+str(case_ids[i]),
       {'status_id':results[i], 'comment': '#URL #github'}
      )
      print("--------------------------")
      print('Test Case Updated,Case id:',case_ids[i])
    i+=1
  




