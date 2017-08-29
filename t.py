#!/opt/bin/python
a = [1,2,3]
b = []
a.append(a)
print a
print a[3][0]
print a + a
b.extend(a)
print b
