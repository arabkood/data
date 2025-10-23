import heapq


class JobScheduler:
    def __init__(self):
        self.jobs = []
        self.counter = 0
        self.job_map = {}

    def add_job(self, job_id, priority, execution_time):
        entry = (execution_time, priority, self.counter, job_id)
        heapq.heappush(self.jobs, entry)
        self.job_map[job_id] = entry
        self.counter += 1

    def get_next_job(self, current_time):
        # Remove jobs that are ready and find the highest priority one
        while self.jobs:
            exec_time, priority, counter, job_id = self.jobs[0]

            if exec_time > current_time:
                return None

            heapq.heappop(self.jobs)
            if job_id in self.job_map:
                del self.job_map[job_id]
                return job_id

        return None

    def remove_job(self, job_id):
        if job_id in self.job_map:
            del self.job_map[job_id]
