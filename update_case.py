
import pprint
from testrail import *

#Sending POST request to TestRail API for updating a test case via case id
client = APIClient('https://cloudbyte.testrail.com/')
client.user='karthik.s@cloudbyte.com'
client.password='openebs'


run_id='1711'
result=open("newtext.txt","r")
file1=result.read()
file1=str(file1)
req=client.send_post('add_results_for_cases/'+run_id,
		{
			'results':[
				{
				 'case_id':166291,
				 'status_id':1,
				 'comment':file1
				}
				]
		}
	
)

pprint.pprint(req)
