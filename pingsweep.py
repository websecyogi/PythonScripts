# A simple Python PingSweep program
#!/usr/bin/env python
import os,subprocess

for i in range(1,10):
        IP = "192.168.100."+str(i)
        NULL = open(os.devnull, 'w')
        if( subprocess.call(["ping", "-c 1", IP], stdout=NULL, stderr=subprocess.STDOUT)) == 0:
                print "Host %s is Alive!!" %IP

print "Done!!"
                                                                                                                              
                   
