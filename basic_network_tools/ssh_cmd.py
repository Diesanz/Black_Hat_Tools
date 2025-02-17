import paramiko

def ssh_command(ip, port,user, passwd, cmd):
	client = paramiko.SSHClient()

	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, port=port, username=user, password=passwd)

	_, stdout, stderr = client.exec_command(cmd)
	output = stdout.readlines() + stderr.readlines()

	if output:
		print('--- Output ---')
		for line in output:
			print(line.strip())

if __name__ == '__main__':
	import getpass
	#user = getpass.getuser()
	user = input('Username: ')
	password = getpass.getpass()

	ip = input('Enter a valid IP: ') or '192.168.1.100'
	port = input('Enter a port or <CR>: ') or 2222
	cmd = input('Enter a command or <CR>: ') or 'id'

	ssh_command(ip, port, user, password, cmd)
