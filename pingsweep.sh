# A simple Ping Sweep shell script
#!/bin/bash
# IP range
ip=192.168.100

for i in $(seq 1 10); do
        ping -c 2  $ip.$i  &> /dev/null
        if [ $? == 0 ]; then echo "Host"  $ip.$i "is Alive!!"; fi

done
