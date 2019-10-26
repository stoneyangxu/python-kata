import os
import queue
from multiprocessing import Process, cpu_count


def search(paths, query_q, result_q):
    lines = []
    for path in paths:
        lines.extend(l.strip() for l in open(path))
    query = query_q.get()
    while query:
        result_q.put_([l for l in lines if query in l])
        print(result_q.qsize())
        query = query_q.get()


if __name__ == '__main__':
    cpus = cpu_count()
    pathnames = [f for f in os.listdir('.') if os.path.isfile(f)]
    paths = [pathnames[i::cpus] for i in range(cpus)]

    query_queue = [queue.Queue(maxsize=10) for p in range(cpus)]
    result_queue = queue.Queue(maxsize=10)

    search_procs = [
        Process(target=search, args=(p, q, result_queue)) for p, q in zip(paths, query_queue)
    ]

    for proc in search_procs:
        proc.start()

    for q in query_queue:
        q.put('def')
        q.put(None)

    print(result_queue.qsize())

    print(result_queue.qsize())

    for r in range(cpus):
        for match in result_queue.get():
            print(match)

    for proc in search_procs:
        proc.join()
