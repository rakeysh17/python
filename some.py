#!/opt/bin/python
import sys
import ast

print "=================="

import sys
import ast

#d = ast.literal_eval(str(sys.argv[1]))
d = str(sys.argv[1]).split(',')
b = (str(sys.argv[2])).split(',')
#b = ast.literal_eval(str(sys.argv[2]))

#print d.split(',')
#print b.split(',')
print d
print b
for a in d:
    print a

for e in b:
    print e
