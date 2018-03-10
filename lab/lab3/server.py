import zmq
import time

SEP = "&&&&&&&&&&&&&&&"

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
rsp_sock = context.socket(zmq.REP)
rsp_sock.bind("tcp://127.0.0.1:13442")
pub_sock = context.socket(zmq.PUB)
pub_sock.bind("tcp://127.0.0.1:13443")


while True:
    msg = rsp_sock.recv_string()
    rsp_sock.send_string('')
    name, content = msg.split(SEP)
    print("Rev from {1}: {0}".format(content, name))
    pub_sock.send_string("{0}{1}{2}".format(name, SEP, content))
    time.sleep(0.1)

