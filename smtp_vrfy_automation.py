#!/bin/python
import socket
import sys

if len(sys.argv) !=4:
	print "\nUsage: smtp_vrfy_automation.py <mail server IP> -u <userlist filepath>\n"
	print "\nUsage: smtp_vrfy_automation.py <mail server IP> -U <username>\n"
	sys.exit(0)

def smtp_verfy(user):
	#create socket for smtp

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect = s.connect((sys.argv[1],25))

	#Receive Banner

	banner = s.recv(1024)
	print banner

	s.send('VRFY '+ user + '\r\n')

	result = s.recv(1024)
	print result

	#Close socket
	s.close()

if "-u" in str(sys.argv[2]):
	print "\n[*] Wordlist selected!. Use '-U' for single user\n"
	with open(sys.argv[3], 'r') as f:
		for user in f:
			user = user.strip()
			print "Checking user: " + str(user)
			smtp_verfy(user)
			sys.exit(0)

elif "-U" in str(sys.argv[2]):
	print "\n[*] Use '-u' for multiple users wordlist\n"
	print "Checking user: " + str(sys.argv[3])
	smtp_verfy(sys.argv[3])

else:
	print("\n[+] Try again!\n")
	sys.exit(0)
