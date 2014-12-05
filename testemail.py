#!C:\Python27\python.exe -u
import smtplib
print "Content-type: text/html\n"
def send_email(from_person,to_person,subject,message):
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login("liubingfeng7","mleonveg")
	header="From:{0}\nTo:{1}\nCc:{1}\nSubject:{2}\n\n".format(from_person,to_person,subject,message)
	message=header+message
	try:
		problems=server.sendmail(from_person,to_person,message)
		print("Sending Email to {0} Success! ^.^".format(to_person))
	except Exception:
		print str(problems);
	server.quit()
#for this to work, need to change the setting of gmail account to let low secure app accessing
#url https://support.google.com/accounts/answer/6010255
send_email("liubingfeng7@gmail.com","liubingfeng7@gmail.com","Python Hello World","Hello World")