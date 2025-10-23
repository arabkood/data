import unittest
from solution import CommandProcessor


class TestCommandProcessor(unittest.TestCase):
    def test_register_and_execute(self):
        processor = CommandProcessor()
        state = {"value": 0}

        def add_exec(x):
            state["value"] += x

        def add_undo(x):
            state["value"] -= x

        processor.register_command("add", add_exec, add_undo)
        processor.execute("add", 5)
        self.assertEqual(state["value"], 5)

    def test_undo(self):
        processor = CommandProcessor()
        state = {"value": 0}

        def add_exec(x):
            state["value"] += x

        def add_undo(x):
            state["value"] -= x

        processor.register_command("add", add_exec, add_undo)
        processor.execute("add", 5)
        processor.execute("add", 3)
        processor.undo()
        self.assertEqual(state["value"], 5)

    def test_history(self):
        processor = CommandProcessor()
        state = {"value": 0}

        def add_exec(x):
            state["value"] += x

        def add_undo(x):
            state["value"] -= x

        processor.register_command("add", add_exec, add_undo)
        processor.execute("add", 5)
        processor.execute("add", 3)
        self.assertEqual(processor.get_history(), ["add", "add"])

    def test_multiple_commands(self):
        processor = CommandProcessor()
        state = {"value": 0}

        def add_exec(x):
            state["value"] += x

        def add_undo(x):
            state["value"] -= x

        def mul_exec(x):
            state["prev"] = state["value"]
            state["value"] *= x

        def mul_undo(x):
            state["value"] = state["prev"]

        processor.register_command("add", add_exec, add_undo)
        processor.register_command("mul", mul_exec, mul_undo)

        processor.execute("add", 5)
        processor.execute("mul", 2)
        self.assertEqual(state["value"], 10)
        processor.undo()
        self.assertEqual(state["value"], 5)

    def test_undo_empty_history(self):
        processor = CommandProcessor()
        processor.undo()


if __name__ == "__main__":
    unittest.main(verbosity=2)
