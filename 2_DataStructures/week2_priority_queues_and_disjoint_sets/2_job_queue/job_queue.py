# python3

import heapq


class workerThread:

    def __init__(self, thread_no, released_time=0):
        self.thread_no = thread_no
        self.released_time = released_time

    def __lt__(self, free_worker_thread):
        assert isinstance(free_worker_thread, workerThread)
        if self.released_time == free_worker_thread.released_time:
            return self.thread_no < free_worker_thread.thread_no
        return self.released_time < free_worker_thread.released_time

    def __str__(self):
        return "{} {}".format(self.thread_no, self.released_time)


class JobQueue:

    def __init__(self, n_workers, jobs):
        self.n_workers = n_workers
        self.workers = [workerThread(id) for id in range(n_workers)]
        self.jobs = jobs

    def schedule_jobs(self):

        for job in self.jobs:
            job_thread = heapq.heappop(self.workers)
            yield str(job_thread)
            job_thread.released_time += job
            heapq.heappush(self.workers, job_thread)


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    job_queue = JobQueue(n_workers, jobs)
    assigned_jobs = job_queue.schedule_jobs()

    for job in assigned_jobs:
        print(job)


if __name__ == "__main__":
    main()
