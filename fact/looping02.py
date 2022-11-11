#!/user/bin/env python3

""" This is file reading class from python
    by Arun """


dnsfile=open("dnsservers.txt","r")

dnslist=dnsfile.readlines()


for svr in dnslist:

    print(svr, end="")



dnsfile.close()
