import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mIP = input()
mPort = input()
sock.bind((mIP, int(mPort)))
while True:
	account = 0
	addrList = []
	dataList = []
	while account<2:
		data,addr = sock.recvfrom(1024)
		tmpMsg = addr[0]+','+data.decode(encoding = "utf-8")
		print(tmpMsg)	# debug 
		addrList.append(addr)
		dataList.append(tmpMsg)
		account += 1

	sock.sendto(dataList[1].encode(encoding = "utf-8"), addrList[0])
	sock.sendto(dataList[0].encode(encoding = "utf-8"), addrList[1])