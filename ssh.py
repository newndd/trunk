import os, sys
import re
import subprocess
import paramiko

def regen(host):
	#	os.system('')
	cmd = "ssh-keygen -R "+host
	print cmd
	os.system(cmd)


def keygen(username):
	cmd = "echo ''|ssh-keygen -t rsa -C "+username+"@e.com # -f "+username+"@e.com"
	os.system(cmd)
	print username


def del_key(keyname):
	with open('test', 'r') as f:
		dd = f.readlines()
	
		for line in dd:
			if keyname in line:
				print "Num: no "+keyname
			else:
				print "Num: "+line

def del_key_bash(keyname):
	cmd = "sed -i '/il@/d' ./test"
	os.system(cmd)
		
	
def add_key(host, username, password, keyname):
	#http://jessenoller.com/blog/2009/02/05/ssh-programming-with-paramiko-completely-different
	ssh = paramiko.SSHClient()
	with open('root@com.pub', 'r') as f: dd = f.readlines()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect('127.0.0.1', username='ilya', password='olegtga1')
	(stdin, stdout, stderr) = ssh.exec_command("echo \""+''.join(dd)+"\">>~/.ssh/testl")
	#type(stdin)
	#print stdout.readlines()
	print stderr
	

host = "127.0.0.1";
regen(host)
username = ""
keygen(username)
root = 'root'
del_key(root)
del_key_bash(root)

home = os.getenv("HOME")
print home
ssh1 = paramiko.SSHClient()
add_key('127.0.0.1', 'username', '1231231', 'key');
