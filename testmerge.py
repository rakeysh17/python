#!/opt/bin/python
print " testing FIFO "
my_list = 'echo "nameserver 8.8.8.8" >> /etc/resolv.conf'

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item))

f.close()
