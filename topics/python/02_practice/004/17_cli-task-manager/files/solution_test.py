import unittest
from solution import TaskManager


class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        tm = TaskManager()
        task_id = tm.add_task("Test task", 1, ["test"])
        self.assertEqual(task_id, 1)

    def test_get_all_tasks(self):
        tm = TaskManager()
        tm.add_task("Task 1", 1, ["tag1"])
        tm.add_task("Task 2", 2, ["tag2"])
        tasks = tm.get_tasks("all")
        self.assertEqual(len(tasks), 2)

    def test_complete_task(self):
        tm = TaskManager()
        task_id = tm.add_task("Task 1", 1, ["tag1"])
        tm.complete_task(task_id)
        completed = tm.get_tasks("completed")
        self.assertEqual(len(completed), 1)
        self.assertEqual(completed[0]["status"], "completed")

    def test_filter_pending(self):
        tm = TaskManager()
        tm.add_task("Task 1", 1, ["tag1"])
        task_id = tm.add_task("Task 2", 2, ["tag2"])
        tm.complete_task(task_id)
        pending = tm.get_tasks("pending")
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0]["title"], "Task 1")

    def test_search_by_tag(self):
        tm = TaskManager()
        tm.add_task("Task 1", 1, ["urgent", "work"])
        tm.add_task("Task 2", 2, ["personal"])
        results = tm.search_by_tag("urgent")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Task 1")

    def test_get_by_priority(self):
        tm = TaskManager()
        tm.add_task("Task 1", 1, ["tag1"])
        tm.add_task("Task 2", 2, ["tag2"])
        tm.add_task("Task 3", 1, ["tag3"])
        results = tm.get_by_priority(1)
        self.assertEqual(len(results), 2)

    def test_delete_task(self):
        tm = TaskManager()
        task_id = tm.add_task("Task 1", 1, ["tag1"])
        tm.delete_task(task_id)
        tasks = tm.get_tasks("all")
        self.assertEqual(len(tasks), 0)

    def test_complex_scenario(self):
        tm = TaskManager()
        tm.add_task("Buy groceries", 1, ["shopping", "urgent"])
        tm.add_task("Read book", 2, ["personal"])
        tm.add_task("Write code", 1, ["work", "urgent"])

        urgent = tm.search_by_tag("urgent")
        self.assertEqual(len(urgent), 2)

        priority_1 = tm.get_by_priority(1)
        self.assertEqual(len(priority_1), 2)

        tm.complete_task(1)
        pending = tm.get_tasks("pending")
        self.assertEqual(len(pending), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
