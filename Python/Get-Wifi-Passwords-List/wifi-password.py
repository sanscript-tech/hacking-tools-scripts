import os
import subprocess
# For Linux OS
if os.name=='posix':
	output = subprocess.run(["nmcli", "-g", "NAME", "connection", "show"], capture_output=True)
	allWifi = output.stdout.decode('utf-8', errors='strict')
	allWifiList = allWifi.split("\n")
	allWifiList.pop()
	wifiPasslist = []
	for wifi in allWifiList:
		password = subprocess.run(["nmcli", "-s", "-g", "802-11-wireless-security.psk", "connection", "show", wifi], capture_output=True)
		wifiPasslist.append(wifi + ": " + password.stdout.decode('utf-8', errors="strict"))
	f = open('wifi-passwords-linux.txt', 'w')
	f.writelines(wifiPasslist)
# For Windows OS
if os.name=='nt':
	output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True)
	allWifi = output.stdout.decode('utf-8', errors='strict')
	allWifiList = allWifi.split('\n')
	completePasswordList = []
	wifiProfileList = []
	for wifi in allWifiList:
		if "All User Profile" in wifi:
			temp = wifi.split(":")
			wifiName = temp[1]
			# Final Profile Name
			wifiName = wifiName[1:-1]
			wifiProfileList.append(wifiName)
	for profile in wifiProfileList:
		output2 = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True)
		allWifi2 = output2.stdout.decode('utf-8', errors='strict')
		allWifiList2 = allWifi2.split('\n')
		for wifi in allWifiList2:
			if "Key Content" in wifi:
				temp2 = wifi.split(":")
				wifiPass = temp2[1]
				# Final Password
				wifiPass = wifiPass[1:-1]
				print("Password : " + wifiPass)
				completePasswordList.append(profile + ": " + wifiPass + "\n")
	f = open('wifi-passwords-win.txt', 'w')
	f.writelines(completePasswordList)