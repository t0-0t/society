from github3 import login
import sys
import base64
import uuid




class Git:
	def __init__(self):
		self.config = dict()
		with open('config/git.cfg', 'r') as git_file:
			output = git_file.read().split('\n')
			self.config['git_username'] = base64.b64decode(output[0]).decode()
			self.config['git_pass'] = base64.b64decode(output[1]).decode()
			self.config['git_repo'] = base64.b64decode(output[2]).decode()
			del output


		try:
			self.git_client = login(self.config['git_username'], self.config['git_pass'])
			self.git_repo = self.git_client.repository('ron1n8', 'society')
			self.git_branch = self.git_repo.branch('master')
			self.git_repo_content = self.getRepoContent()
			
		except Exception as e:
			print('Error >> ', e)




	def getRepoContent(self):

		tree = self.git_branch.commit.commit.tree.to_tree().recurse()
		files = list()
		raw_files = list()

		for file in tree.tree:
			raw_files.append(file)
			files.append(file.path)


		return {'plain': files, 'raw': raw_files}


	def getPlainFileContent(self, file):
		return base64.b64decode(self.git_repo.blob(file._json_data['sha']).content)



	def updateLocalFiles(self):
		...


	def sendData(self):
		...



if __name__ == '__main__':
	# git_object = Git()
	print(uuid.uuid4().hex)