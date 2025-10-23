class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.counter = 0

    def add_task(self, title, priority, tags):
        self.counter += 1
        task_id = self.counter
        self.tasks[task_id] = {
            "id": task_id,
            "title": title,
            "priority": priority,
            "tags": tags,
            "status": "pending"
        }
        return task_id

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = "completed"

    def get_tasks(self, filter_by="all"):
        if filter_by == "all":
            return list(self.tasks.values())
        elif filter_by == "pending":
            return [task for task in self.tasks.values() if task["status"] == "pending"]
        elif filter_by == "completed":
            return [task for task in self.tasks.values() if task["status"] == "completed"]
        return []

    def search_by_tag(self, tag):
        return [task for task in self.tasks.values() if tag in task["tags"]]

    def get_by_priority(self, priority):
        return [task for task in self.tasks.values() if task["priority"] == priority]

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
