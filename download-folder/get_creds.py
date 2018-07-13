#This file Reads credentials from a JSON filie

import json

def credentials():
  credential_file=open('creds/credentials.json','r')
  credential=json.loads(credential_file.read())

  username=credential["user"]
  password=credential["password"]
  return username,password

