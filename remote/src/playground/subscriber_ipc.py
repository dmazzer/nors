import zmq, json

def main():
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.bind("ipc:///tmp/test.pipe")
    subscriber.setsockopt(zmq.SUBSCRIBE, '')
    while True:
        print subscriber.recv()

if __name__ == "__main__":
    main()