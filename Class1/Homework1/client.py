# setup
import socket
import sys
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
s.sendall(b'cs5700spring2017 HELLO 1\n')
data = s.recv(1024)

# recieve STATUS
print('Received', repr(data))

# create SOLUTION function
def createSolution(num1, operator, num2):
	if (operator == "+"):
		return num1 + num2
	elif (operator == "-"):
		return num1 - num2
	elif (operator == "*"):
		return num1 * num2
	elif (operator == "/"):
		return math.floor(num1 / num2)
	else:
		return num1 + num2

# return solution



# handle BYE
s.close()


# debugging stuff
print('arguments are ',sflag,', ',pflag,', ',hname,', ',nuid,', ')