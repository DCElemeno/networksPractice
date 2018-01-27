# setup
import socket
import sys
import math
args = sys.argv

# grab arguments
sflag = args[1].strip()
pflag = args[2].strip()
hname = args[3].strip()
nuid = args[4].strip()

# create tcp socket connection
host = socket.gethostname()
port = 27994
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# once connected send HELLO message
s.sendall(b'cs5700spring2018 HELLO 1\n')
data = s.recv(1024)

# recieve STATUS
print(data.decode())

# create SOLUTION function
def createSolution(num1, operator, num2):
	if (operator == "+"):
		return num1 + num2
	elif (operator == "-"):
		return num1 - num2
	elif (operator == "*"):
		return num1 * num2
	elif (operator == "/"):
		return int(num1 // num2)
	else:
		print("fucked up")
		return num1 + num2

# set vals
def sendSolution(d):
	
	# setup
	parsed = d.decode().split(" ")
	firstArg = int(parsed[2])
	operator = parsed[3]
	secondArg = int(parsed[4].split("\n")[0])

	# return
	solution = createSolution(firstArg, operator, secondArg)
	msg = 'cs5700spring2018 '+str(solution)+'\n'
	s.sendall(msg.encode())
	response = s.recv(1024)

	# log to terminal
	print(msg)
	print(response.decode())

	# recurse or end
	if "BYE" not in response.decode():
		sendSolution(response)
	else:
		print(d.decode().split(" ")[0])
		s.close()


# call function
sendSolution(data)

# debugging stuff
# print('arguments are ',sflag,', ',pflag,', ',hname,', ',nuid,', ')