#!/usr/local/bin/python
#
import sys
# the next line tells the script to read from stdin and use it for output
output = sys.stdin.read()
#the next line tells the script where to save the output
outfile = open('/tmp/file.txt', 'w')
#the next line tells the script to consider the file as stdout instead of the console
sys.stdout = outfile
#print the output from stdin into the file
print output
#close the file!
outfile.close()
