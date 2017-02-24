'''
Created on 24.02.2017

@author: steinorb
'''
import paramiko
import traceback
import socket
import sys


paramiko.util.log_to_file('log/deploy.log')

UseGSSAPI = True             # enable GSS-API / SSPI authentication
DoGSSAPIKeyExchange = True
Port = 22
username = 'pi'
hostname = 'raspberry'
password = 'facharbeit'

# get host key, if we know one
hostkeytype = None
hostkey = None

# now, connect and use paramiko Transport to negotiate SSH2 across the connection
try:
    t = paramiko.Transport((hostname, Port))
    t.connect(hostkey, username, password, gss_host=socket.getfqdn(hostname),
              gss_auth=UseGSSAPI, gss_kex=DoGSSAPIKeyExchange)
    sftp = paramiko.SFTPClient.from_transport(t)

    # dirlist on remote host
    dirlist = sftp.listdir('.')
    print("Dirlist: %s" % dirlist)
    
    # create directory and copy files
    try:
        sftp.mkdir("multimeter")
    except IOError:
        print('(assuming demo_sftp_folder/ already exists)')

    sftp.put('auswahl.py', 'multimeter/auswahl.py')
    
except Exception as e:
    print('*** Caught exception: %s: %s' % (e.__class__, e))
    traceback.print_exc()
    try:
        t.close()
    except:
        pass
    sys.exit(1)        