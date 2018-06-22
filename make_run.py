
from testrail import * 
import pprint

client = APIClient('https://cloudbyte.testrail.com')
client.user = 'karthik.s@cloudbyte.com'
client.password = 'openebs'

case = client.send_post(
	'add_run/1' , 
	{ 'suite_id':795 , 'name':'openebs_test_run#s' , 'description':'made for adding description and testing API call' }
)

run_id=case['id']
addr='add_results_for_cases/'+str(run_id)

res_update=client.send_post(
		addr,
		{
			"results":[
				{
				 "case_id":166292,
				 "status_id":1,
				 "comment": "Test Passed Successfully!(API testing)"
				},
				{
				 "case_id":166291,
				 "status_id":5,
				 "comment":"Test failed!(API testing)",
				 "defects": "Fail (defected)"
				}
]
}
)


pprint.pprint(res_update)
