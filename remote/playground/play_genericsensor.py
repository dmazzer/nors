
#!/usr/bin/env python2


import time
import zmq
import random

def consumer():
    consumer_id = random.randrange(1,10005)
    print "I am consumer #%s" % (consumer_id)
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5155")
    
    while True:
        work = consumer_receiver.recv_json()
        print(work)

consu