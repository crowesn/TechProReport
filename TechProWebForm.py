#TechProWebForm.py
import os, subprocess, sys

if len(sys.argv) < 4:
	print '<font color="red">Script requires email, login, and password!</font>'
	sys.exit()

elif len(sys.argv) == 4:
	SessionUser = sys.argv[1]
	SessionPass = sys.argv[2]
	Recipient1 = sys.argv[3]
else:
	print '<font color="red">Login Error, check your username and pass</font>'
	sys.exit()
if Recipient1 != 'max.abel@uc.edu' and Recipient1 != 'sean.crowe@uc.edu' and Recipient1 != 'james.vanmil@uc.edu' and Recipient1 != 'jeff.crawford@uc.edu' and Recipient1 != 'lorna.newman@uc.edu':
	print '<font color="red">Invalid email!</font>'
	sys.exit()
#print SessionUser, SessionPass, Recipient1
FNULL = open('/dev/null', 'w')
b = subprocess.Popen(['python', 'TechProCheck.py', SessionUser, SessionPass, Recipient1], stdout=FNULL, stderr=FNULL)
if b.pid != '':
	print '<h2><font color="green">Script initiated; your report will arrive via email ~5 mins<br>Please close this window</font></h2>'

#raw_input('Script is running')
