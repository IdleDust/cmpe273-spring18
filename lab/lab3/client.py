import zmq
import time
import threading
import sys
# from global_constant import *

SEP = "&&&&&&&&&&&&&&&"

# user name
name = sys.argv[1]

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
req_sock = context.socket(zmq.REQ)
req_sock.connect("tcp://127.0.0.1:13442")
sub_sock = context.socket(zmq.SUB)
sub_sock.setsockopt_string(zmq.SUBSCRIBE, "")
sub_sock.connect("tcp://127.0.0.1:13443")


class ReqThread(threading.Thread):
    def run(self):
        while True:
            msg = input()
            req_sock.send_string("{0}{1}{2}".format(name, SEP, msg))
            req_sock.recv_string()
            time.sleep(0.1)


class SubThread(threading.Thread):
    def run(self):
        while True:
            msg = sub_sock.recv_string()
            endindex = 1 + len(name)
            msg_list = msg.split(SEP)
            if msg_list[0] == name:
                continue
            print("[{0}]: {1}".format(msg_list[0], msg_list[1]))


req_thread = ReqThread()
sub_thread = SubThread()

req_thread.start()
sub_thread.start()

req_thread.join()
sub_thread.join()

