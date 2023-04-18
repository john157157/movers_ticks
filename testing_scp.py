# # from paramiko import SSHClient
# # from scp import SCPClient

# HOST = '45.33.74.44'
# USER = 'john'
# # with SSHClient() as ssh:
# #     ssh.load_system_host_keys()
# #     # ssh.connect('example.com')
# #     # ssh.connect(HOST)
# #     ssh.connect(HOST, username=USER, look_for_keys=False)

# #     with SCPClient(ssh.get_transport()) as scp:
# #         scp.put('sample.txt')
# #         # scp.get('test2.txt')


# from paramiko import SSHClient
# from scp import SCPClient

# ssh = SSHClient()
# ssh.load_system_host_keys()
# ssh.connect(HOST, username=USER)

# with SCPClient(ssh.get_transport()) as scp:
#    scp.put('sample.txt')


import os

os.system("scp ~/Documents/PythonCode/stocks/sample.txt john@45.33.74.44:~/Documents/PythonCode/stocks")
