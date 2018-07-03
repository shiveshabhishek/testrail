from testrail import * 
from make_github_issue import *
import pprint
import csv

#Setting up credentials and URL
client = APIClient('https://cloudbyte.testrail.com')
client.user = '-----------'
client.password = '----------'


case_ids=[]
results=[]
with open("newcsv.csv") as csvfile:
    csvfile = csv.DictReader(csvfile)
    for row in csvfile:
        case_id=row['case_id']
        case_ids.append(case_id)
        suite_id=row['suite_id']

        result=row['status']
        if str(result)=='Test Passed':
            result=1
        else:
            result=5
        results.append(result)

size=len(case_ids)

run=client.send_post(
    'add_run/3',
    {'suite_id': suite_id, 'description': 'Testing for creation via API'}
)
run_id=run['id']
print('Run ID:',run_id)
i=0
for cases in set(case_ids):
    add_result=client.send_post(
        'add_result_for_case/'+str(run_id)+'/'+str(case_ids[i]),
        {'status_id':results[i], 'comment': '#URL #github'}
    )
    comment=add_result['comment']
    print('Comment:',comment)
      
    #Checking ,if result fails then create one Github Issue
    if results[i]==5:
        make_github_issue('TR-issue', 'Case ID: '+case_ids[i]+' Suite ID: '+suite_id+' Comment: '+comment ,'shiveshabhishek' , ['test'])
    #    print('Isuue created for case_id:',case_ids[i])
    print("--------------------------")
    i+=1
      