#TechProCheck.py
import sys, subprocess, os


#Get Mil Profile arguments
if len(sys.argv) < 4:
	print 'Script requires email, login, and password!'
	sys.exit()

elif len(sys.argv) == 4:
	SessionUser = sys.argv[1]
	SessionPass = sys.argv[2]
	Recipient1 = sys.argv[3]
else:
	print 'Login Error, check your username and pass'
	sys.exit()

def sendMail(x):
	sendmail_location = "/usr/sbin/sendmail" # sendmail location
	p = os.popen("%s -t" % sendmail_location, "w")
	p.write("From: %s\n" % "errors@TechProReport.uc.edu")
	p.write("To: %s, sean.crowe@uc.edu\n" % Recipient1)
	p.write("Subject: TechPro report: fatal error\n")
	p.write("\n") # blank line separating headers from body
	p.write(x)
	status = p.close()
	if status != 0:
		print "Sendmail exit status", status

def submit_query(SessionUser, SessionPass, Recipient1):
	query = os.popen("PGPASSWORD={1} /UCUsers/Users/c/crowesn/eresources/pgsq/bin/psql -A -H -U {0} -h 10.40.2.228 -p 1032 -d iii -f /UCUsers/Users/c/crowesn/eresources/pgsq/scripts/TechProReport.psql 2>&1 | mail -s \"TechPro Report\nContent-Type:text/html\" {2}, sean.crowe@uc.edu".format(SessionUser, SessionPass, Recipient1))
try:
	#connect to host and login

	submit_query(SessionUser, SessionPass, Recipient1)

except: 
	print "Unexpected error:", sys.exc_info()[0]
	sendMail(str(sys.exc_info()))

