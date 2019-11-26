import re
ip = '192.168.2.1'
var = re.match(r'\d{3}\.\d{3}.\d\.\d', ip)
print(var)
re.findall(r'\d{3}\.\d{3}.\d\.\d', ip)