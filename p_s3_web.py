#!/bin/python

#Import subprocess for OS related command
import subprocess

file = open("/tmp/s3_g_get.txt", 'r')

#Get s3 bucket name in a list
s3_bucket = []
line = file.readline()

#While loop for appending bucket names to s3_bucket list
while line != '':
    s3_bucket.append(line.rstrip('\n'))
    line = file.readline()
file.close()
#print s3_bucket

#For loop for getting the s3 web settings
dict = {}

for i in s3_bucket:
#    print i
#    subprocess.call('aws s3api get-bucket-website --bucket '+i, shell=True)
    dict[i] = subprocess.call('aws s3api get-bucket-website --bucket '+i, shell=True)

#inverting dict
invert_dict = {}

for j in dict:
    code = dict[j]
    if not (code in invert_dict):
        invert_dict[code] = [j]
    else:
        invert_dict[code].append(j)

print invert_dict
