import unittest
from solution import JobScheduler


class TestJobScheduler(unittest.TestCase):
    def test_single_job(self):
        scheduler = JobScheduler()
        scheduler.add_job("job1", 1, 10)
        self.assertEqual(scheduler.get_next_job(10), "job1")

    def test_priority_order(self):
        scheduler = JobScheduler()
        scheduler.add_job("job1", 2, 10)
        scheduler.add_job("job2", 1, 10)
        self.assertEqual(scheduler.get_next_job(10), "job2")
        self.assertEqual(scheduler.get_next_job(10), "job1")

    def test_time_constraint(self):
        scheduler = JobScheduler()
        scheduler.add_job("job1", 1, 10)
        scheduler.add_job("job2", 1, 5)
        self.assertEqual(scheduler.get_next_job(5), "job2")
        self.assertIsNone(scheduler.get_next_job(9))
        self.assertEqual(scheduler.get_next_job(10), "job1")

    def test_remove_job(self):
        scheduler = JobScheduler()
        scheduler.add_job("job1", 1, 10)
        scheduler.add_job("job2", 2, 10)
        scheduler.remove_job("job1")
        self.assertEqual(scheduler.get_next_job(10), "job2")

    def test_complex_scenario(self):
        scheduler = JobScheduler()
        scheduler.add_job("job1", 2, 10)
        scheduler.add_job("job2", 1, 10)
        scheduler.add_job("job3", 1, 5)
        self.assertEqual(scheduler.get_next_job(5), "job3")
        self.assertEqual(scheduler.get_next_job(10), "job2")
        self.assertEqual(scheduler.get_next_job(10), "job1")

    def test_no_jobs_ready(self):
        scheduler = JobScheduler()
        scheduler.add_job("job1", 1, 10)
        self.assertIsNone(scheduler.get_next_job(5))


if __name__ == "__main__":
    unittest.main(verbosity=2)
