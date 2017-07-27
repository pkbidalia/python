#!/usr/bin/python

import re, sys
ip = []
file = "/Users/pravesh/Downloads/apache_log.log"

def ipList():
    with open(file, "r") as f:
        for line in f:
            #matchObj = re.search(r'(\d+.\d+.\d+.\d+).*(DELETE|PUT|GET|POST)\s/.*/1.0"\s+(\d{3})', line)
            ipObj = re.search(r'(\d+.\d+.\d+.\d+)', line)
            if ip.count(ipObj.group()) == 0:
                ip.append(ipObj.group())
        return ip

def countReqPerIP(ip):
    getC = 0
    postC = 0
    deleteC = 0
    putC = 0
    with open(file, "r") as f:
        for line in f:
            ipObj = re.search(r'(\d+.\d+.\d+.\d+)', line)
            #print ipObj.group()
            reqObj = re.search(r'.*(DELETE|PUT|GET|POST)\s/.*', line)
            #print reqObj.group(1)
            if ip == ipObj.group():
                if reqObj.group(1) == "PUT":
                    putC+=1
                elif reqObj.group(1) == "POST":
                    postC+=1
                elif reqObj.group(1) == "DELETE":
                    deleteC+=1
                elif reqObj.group(1) == "GET":
                    getC+=1
                else:
                    print "Quiting not matching any type of request"
        print "%s: GET=%s PUT=%s POST=%s DELETE=%s " % (ip, str(getC), str(putC), str(postC), str(deleteC))

ipArray = ipList()
for ip in ipArray:
    countReqPerIP(ip)
