#!/bin/env bash
count=`/usr/bin/python3 /home/hp/scripts/tplink_helper.py get_status|grep -o 0.0.0.0|wc -l`
if [ $count -ge 5 ]; then
    /usr/bin/python3 /home/hp/scripts/tplink_helper.py login
fi
