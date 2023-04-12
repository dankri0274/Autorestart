import os
import time
import ctypes

# Declaring variables
furtherPostponing = True

lib = ctypes.windll.kernel32
t = lib.GetTickCount64()
t = int(str(t)[:-3])

mins, sec = divmod(t, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)

if os.path.isfile('restart.txt'):
	with open('restart.txt', 'r') as f:
		restartPostponed = f.read()
		if restartPostponed == "postponed":
			furtherPostponing = False

if days >= 5:
	# ctypes.windll.user32.MessageBoxW(0, f"The PC has not been restarted for {days} days, restarting now", "Restart required", 0)
	# subprocess.run(["powershell", "-Command", "Restart-Computer"]) # Specifying to run in PowerShell and not command prompt (cmd)

	print(f"\nThe PC has not been restarted for {days} days, restarting now")
	choice = input("Type \'R\' to continue with restart or \'D\' to postpone restart")

	if choice == "R" or choice == "r":
		os.system("shutdown /r /t 0")
	else:
		if furtherPostponing:
			print("Restart has been postponed")
			with open('restart.txt', 'w') as f:
				f.write('postponed')
			input("Press ENTER to exit")
		else:
			print("Further postponing of restart is not allowed\nRestarting now")
			time.sleep(3)
			os.system("shutdown /r /t 0")
else:
	# Mesage, Title, Type of dialog box
	# ctypes.windll.user32.MessageBoxW(0, f"Time since last restart: {days}d, {hour}h, {mins}m.\nThe PC will automatically restart on startup after 5 days", "No restart required", 0)

	print(f"\nTime since last restart: {days}d, {hour}h, {mins}m.\nThe PC will automatically restart on startup after 5 days")
	input("Press ENTER to exit")
