from threading import Thread
from queue import Queue
import random
import time

class Alice(Thread):

    def __init__(self, queue):
        super().__init__()
        self._queue = queue

    def run(self) -> None:
        print("start Alice thread")

        while True:
            time.sleep(random.randint(1, 2))
            i = random.randint(1, 3)
            if i > 1 and queue.qsize() < 100:
                self._queue.put("Message is {}".format(i))


class Bob(Thread):
    def __init__(self, queue):
        super().__init__()
        self._queue = queue

    def run(self) -> None:
        print("start Bob thread")
        while True:
            time.sleep(2)
            while queue.qsize() > 0:
                print("Received message is \"{}\"".format(queue.get()))


if __name__ == '__main__':
    queue = Queue(200)
    alice = Alice(queue)
    alice.start()

    bob = Bob(queue)
    bob.start()
