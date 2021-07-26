from github3 import login
import sys
import base64
import uuid
import os


class Git:
	def __init__(self):
		self.config = dict()
		self.config['git_username'] = base64.b64decode('dDAtMHQ=').decode()
		self.config['git_pass'] = base64.b64decode('U2V4eVBlZ2FzQEA3').decode()
		self.config['git_repo'] = base64.b64decode('c29jaWV0eQ==').decode()


		try:
			self.git_client = login(self.config['git_username'], self.config['git_pass'])
			self.git_repo = self.git_client.repository(self.config['git_username'], self.config['git_repo'])
			self.git_branch = self.git_repo.branch('master')
			self.git_repo_content = self.getRepoContent()
			
		except Exception as e:
			print('Error >> ', e)




	def getRepoContent(self):

		tree = self.git_branch.commit.commit.tree.to_tree().recurse()
		files = dict()

		for file in tree.tree:
			files[file.path] = file


		return files


	def getPlainFileContent(self, file):
		return base64.b64decode(self.git_repo.blob(file._json_data['sha']).content)



	def updateLocalFiles(self):
		for file in self.git_repo_content.keys():
			if len(file.split('.')) == 1:
				print('Directory', file)
			else:
				print('Rewriting', file)
				self.rewriteModule({'path': file, 'content': self.git_repo_content[file]})


	def rewriteModule(self, file):
		if len(file['path'].split('/')) > 1:
			try:
				route = file['path'].split('/')
				route.remove(route[len(route)-1])
				os.makedirs('/'.join(route))
			except Exception as e:
				print(e)
		with open(file['path'], 'w') as module_file:
			module_file.write(self.getPlainFileContent(file['content']).decode())


	def sendData(self):
		...



if __name__ == '__main__':
	git_object = Git()
	git_object.updateLocalFiles()
