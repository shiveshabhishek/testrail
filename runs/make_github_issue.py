#Got the syntax from https://gist.github.com/JeffPaine/3145490
import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'shiveshabhishek'
PASSWORD = '-----'

# The repository to add this issue to
REPO_OWNER = 'shiveshabhishek'
REPO_NAME = 'test'

def make_github_issue(title, body=None, assignee=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.session()
    session.auth=(USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body,
             'assignee': assignee,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print ('Successfully created Issue ', title)
    else:
        print ('Could not create Issue ', title)
        print ('Response:', r.content)

#make_github_issue('Test Issue 2', 'Creating Issue via GITHUB API','shiveshabhishek' , ['test'])