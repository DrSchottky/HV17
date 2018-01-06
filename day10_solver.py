import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('80.74.140.188', 1037))
data = ""
while data.find("HV17") == -1:
	s.send("\n7\n3\n9\n6\n")
	data = s.recv(1024)
pos = data.find("HV17")
print "Flag: " + data[pos : pos+29]
