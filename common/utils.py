
# python3.6

import traceback
from queue import Queue, Empty
from multiprocessing.dummy import Pool


class MyPool:
    def __init__(self, n=5):
        self.queue = Queue()
        self.pool = Pool(n)
        self.n = n

    def start(self):
        self.pool.map_async(self.run, range(self.n))

    def stop(self):
        self.pool.close()
        self.pool.join()

    def run(self, i):
        while True:
            try:
                req = self.queue.get(timeout=1)
                self.process(req, i)
                self.queue.task_done()
            except Empty:
                pass
            except:
                traceback.print_exc()
                self.queue.task_done()

    @property
    def count(self):
        return self.queue.unfinished_tasks

    def put(self, req):
        self.queue.put(req)

    def process(self, req, i):
        pass
