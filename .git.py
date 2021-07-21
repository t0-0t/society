from github3 import login, GitHub
import sys
import base64


config = dict()


with open('config/git', 'r') as git_file:
	output = git_file.read().split('\n')
	config['git_username'] = base64.b64decode(output[0]).decode()
	config['git_pass'] = base64.b64decode(output[1]).decode()
	config['git_repo'] = base64.b64decode(output[2]).decode()
	del output


try:
	git_client = login(config['git_username'], config['git_pass'])