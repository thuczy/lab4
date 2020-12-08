import socket

sock, sockP2P = socket.socket(socket.AF_INET, socket.SOCK_DGRAM),socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverIP = input()
serverPort = input()
mIP = input()
success = 0
clientPort = input()
sockP2P.bind((mIP, int(clientPort)))
sock.sendto(clientPort.encode(encoding = "utf-8"), (serverIP, int(serverPort)))
data,addr = sock.recvfrom(1024)
pairAddr = data.decode(encoding = "utf-8").split(',')
sockP2P.sendto(b"ACK", (pairAddr[0], int(pairAddr[1])))
data,addr = sockP2P.recvfrom(1024)
print("---- (Iport:%d, raddr:%s, rport:%d) ----"%(int(clientPort),pairAddr[0],int(pairAddr[1])))
success = 1

while True:
	choice = input("To send(0) or to listen(1)? : ")
	try:
		choice=int(choice)
		if choice == 0:
			msg = input("Input message:")
			sockP2P.sendto(msg.encode(encoding = "utf-8"), (pairAddr[0], int(pairAddr[1])))
		elif choice == 1:
			print("Listening...")
			data,addr = sockP2P.recvfrom(1024)
			print("Get message [",data.decode(encoding = "utf-8"),"] from addr ", addr[0])
		else:
			print("Invalid, input 0 or 1")
	except:
		print("Invalid, input 0 or 1")