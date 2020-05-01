import personal_login
from personal_login import main
my=main()
#Ignore this lines this is calling my personal logins from another file.please provide your logins below



#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################  
# pip install paramiko
# Paramiko is native library for SSH allother library are created on top of it.


import paramiko
import time

#Provide your login below
host=my['host']
login=my['login']
password=my['password']


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=login, password=password, look_for_keys=False, allow_agent=False)
# Use any of this Method 

############################################################################################################################
#  1. The exec command takes a command as an "argument" and executes it in an isolated environment without terminal emulation
# series of command not work in this which are dependent of each other. All command will run independently.
# much faster than Terminal
#############################################################################################################################

stdin , stdout, stderr = client.exec_command('pwd')
error = stderr.read()
data = stdout.read()
if error:
	print(error.decode("utf-8"))
    
if data:
	print("This output by Exec command",data.decode("utf-8"))
    


############################################################################################################################
#   2.  The shell channel executes a login shell (as if you login with SSH terminal client). The shell will then present a
#command prompt and wait for client/user to type the commands. The purpose of the shell channel is to implement an interactive shell session.
############################################################################################################################


shell_object = client.invoke_shell()
time.sleep(3)
shell_object.send("\n")
time.sleep(4)
cmd='pwd'
shell_object.send(cmd + "\n")
time.sleep(3)
output = str(shell_object.recv(999999).decode("utf-8"))

#print("This output is generated by Terminal: ", output)  #whole output
print("This output is generated by Terminal: ", output.split(cmd)[-1])# only command output rest we are ignoring(split by cmd nd save in list then take it last value.)
 