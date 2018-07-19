
from testrail import * 
import pprint

client = APIClient('https://cloudbyte.testrail.com')
client.user = '----'
client.password = '----'

plan=client.send_get('get_plan/2354')

pprint.pprint(plan)
