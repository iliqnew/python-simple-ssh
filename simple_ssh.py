import paramiko
import getpass

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = input("Enter the hostname: ")
port = 22
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
ssh.connect(host, port, username, password)

while True:
    command = input("> ")
    if command == "exit":
        break
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()
    print(output)

ssh.close()
