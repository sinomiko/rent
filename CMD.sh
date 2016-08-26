#########################################################################
# File Name: CMD.sh
# Author: Miko Song
# Created Time: Fri 26 Aug 2016 02:36:59 PM CST
#########################################################################
#!/bin/bash
python craw_lianjia.py 

sleep 100

python -m SimpleHTTPServer 3000
