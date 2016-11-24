import zmq, json, time
from random import random

def main():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.connect("ipc:///tmp/test.pipe")
    k = round(random()*100)
    while True:
        publisher.send( str("hello world" + str(int(k))) )
        time.sleep( 1 )

if __name__ == "__main__":
    main()
    