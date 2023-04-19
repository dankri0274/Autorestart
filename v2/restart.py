import os
import time
import ctypes

# Declaring variables
furtherPostponing = True
restartAfterDays = 5

lib = ctypes.windll.kernel32
t = lib.GetTickCount64()
t = int(str(t)[:-3])

mins, sec = divmod(t, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)

def clearRestartFile():
	with open('restart.txt', 'r+') as f:
		contents = f.read()
		if "restarted" in contents:
			f.seek(0)
			f.truncate()

if os.path.isfile('restart.txt'):
	with open('restart.txt', 'r+') as f:
		if f.read() == "restarted":
			furtherPostponing = True
			clearRestartFile()
		else:
			furtherPostponing = False

if days >= restartAfterDays:
	print(f"\nThe PC has not been restarted for {days} days, restarting now")
	choice = input("Type \'R\' to continue with restart or \'D\' to postpone restart\n> ")

	if choice.lower() == "r":
		os.system("shutdown /r /t 0")
	else:
		if furtherPostponing:
			print("Restart has been postponed")
			with open('restart.txt', 'w') as f:
				f.write('restarted')
			input("Press ENTER to exit")
		else:
			print("Further postponing of restart is not allowed\nRestarting now")
			with open('restart.txt', 'w') as f:
				f.write('restarted')
			time.sleep(3)
			os.system("shutdown /r /t 0")
else:
	print(f"\nTime since last restart: {days}d, {hour}h, {mins}m.\nThe PC will automatically restart on startup after {restartAfterDays} days")
	input("Press ENTER to exit\n")
