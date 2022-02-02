import os
import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
AUTH_TOKEN = 'API token generated from github'

# The repository to add this issue to
REPO_OWNER = 'Owner of repo'
REPO_NAME = 'Name of repo'


def make_github_issue(title, body=None, labels=[]):
    # Create an issue using the parameters of this function
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)

    # Create an authenticated session to create the issue
    session = requests.Session()
    # Create our issue and headers to authenticate
    headers = {'Authorization': 'token %s' % AUTH_TOKEN,
               'Accept': 'application/vnd.github.v3+json'}
    issue = {'title': title,
             'body': body,
             'labels': labels
             #  'created_at': created_at,
             #  'closed_at': closed_at,
             #  'updated_at': updated_at,
             #  'assignee': assignee,
             #  'milestone': milestone,
             #  'closed': closed
             }

    # Add the issue to our repository
    r = session.post(url, data=json.dumps(issue), headers=headers)
    if r.status_code == 201:
        print('Successfully created Issue {0:s} #{1}'.format(
            title, r.json().get("number")))
    else:
        print('Could not create Issue {0:s}'.format(title))
        print('Response:', r.content)


def update_issue(num):
    url = 'https://api.github.com/repos/%s/%s/issues/%s' % (
        REPO_OWNER, REPO_NAME, num)

    # Create an authenticated session to create the issue
    session = requests.Session()
    # Create our issue and headers to authenticate
    headers = {'Authorization': 'token %s' % AUTH_TOKEN,
               'Accept': 'application/vnd.github.v3+json'}
    issue = {
        'state': 'closed'
        #  'created_at': created_at,
        #  'closed_at': closed_at,
        #  'updated_at': updated_at,
        #  'assignee': assignee,
        #  'milestone': milestone,
        #  'closed': closed
    }

    # Add the issue to our repository
    r = session.patch(url, data=json.dumps(issue), headers=headers)
    if r.status_code == 200:
        print('Successfully Closed Issue #{0}:{1}'.format(
            r.json().get("number"), r.json().get("title")))
    else:
        print('Could not modify Issue #{0}'.format(num))
        print('Response:', r.content)


# update_issue()
# make_github_issue("fifth place", '''
# ## Request details

# Please specify the content of the request.

# ### Things to note:

# - Please assign this issue to a member.
# - Please be sure to set a due date for this request.
# - Notifications for: @Janus and @Toby1980 (add your member's unique id for mentions)
# ''', ["bug", "urgent"])
