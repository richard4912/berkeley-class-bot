import os

def mail(destination, subject, message):
	os.system('sendemail -f mailer-daemon@richard4912.me -t ' + destination + ' -u "' + subject + '" -m "' + message + '"'