from threading import Thread


def threadOneFunction():
    print("ThreadOneFunction running...")


def threadTwoFunction():
    print("ThreadTwoFunction running...")


if __name__ == '__main__':
    print("Starting...")
    t1 = Thread(target=threadOneFunction)
    t2 = Thread(target=threadTwoFunction)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done.")
