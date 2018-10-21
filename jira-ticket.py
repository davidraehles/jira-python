

#!/usr/bin/env python
from jira import JIRA

# set options, e.g. server you want to use
options = {
    'server': 'https://company.atlassian.net'}

# set authentication options
key_cert_data = None
with open('/keys/private.pem', 'r') as key_cert_file:
    key_cert_data = key_cert_file.read()

oauth_dict = {
    'access_token': 'XXX',
    'access_token_secret': 'YYY',
    'consumer_key': 'python-jira-automation',
    'key_cert': key_cert_data
}

# create jira object
jira = JIRA(options, oauth=oauth_dict)

# setting project to Analytics with ID
# jira.projects() shows all available projects with ids
project = jira.project('10001')

# create a new issue from dictionary with all required fields
issue_dict = {
    'project': {'id': 10001},  # The static project ID for AN aka Analytics
    'summary': 'Maybe the last test ticket from jira-python',  # This is the title of the ticket aka summary
    'description': 'Look into this one and close it! (Just a test  )',
    'issuetype': {'name': 'Task'},  # Issue type should always be Task
    'priority': {'name': 'Low'},  # here you can adjust the prio to Critical, High, Medium or Low
    'assignee': {'name': 'david.raehles'},
}
new_issue = jira.create_issue(fields=issue_dict)
new_issue.update(reporter={'name': 'david.raehles'})
# source https://jira.readthedocs.io/en/latest/examples.html
