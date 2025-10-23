import unittest
from solution import processStates


class TestProcessStates(unittest.TestCase):
    def test_simple_transitions(self):
        result = processStates(
            "idle",
            ["start", "stop"],
            {("idle", "start"): "running", ("running", "stop"): "idle"}
        )
        self.assertEqual(result, "idle")

    def test_single_transition(self):
        result = processStates(
            "off",
            ["turn_on"],
            {("off", "turn_on"): "on", ("on", "turn_off"): "off"}
        )
        self.assertEqual(result, "on")

    def test_no_events(self):
        result = processStates("idle", [], {("idle", "start"): "running"})
        self.assertEqual(result, "idle")

    def test_undefined_transition(self):
        result = processStates(
            "idle",
            ["unknown"],
            {("idle", "start"): "running"}
        )
        self.assertEqual(result, "idle")

    def test_multiple_transitions(self):
        result = processStates(
            "a",
            ["go_b", "go_c"],
            {("a", "go_b"): "b", ("b", "go_c"): "c"}
        )
        self.assertEqual(result, "c")


if __name__ == "__main__":
    unittest.main(verbosity=2)
