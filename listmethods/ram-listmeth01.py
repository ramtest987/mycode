#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
with open( "/var/tmp/t1.out", 'w') as f:
   print(proto, end='>', file=f)
   #print(proto, sep='|', end='>', file=f)
#print(proto, sep='|', end='>', file.write('/var/tmp/t1.out'))
#print(proto[1])
#proto.extend("dns") # this line will add d, n, and s
#print(proto)

