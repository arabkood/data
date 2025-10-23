import unittest
from solution import EventSystem


class TestEventSystem(unittest.TestCase):
    def test_single_subscriber(self):
        events = EventSystem()
        results = []

        def handler(data):
            results.append(data)

        events.subscribe("test", handler)
        events.emit("test", "message1")
        self.assertEqual(results, ["message1"])

    def test_multiple_subscribers(self):
        events = EventSystem()
        results = []

        def handler1(data):
            results.append(f"h1:{data}")

        def handler2(data):
            results.append(f"h2:{data}")

        events.subscribe("test", handler1)
        events.subscribe("test", handler2)
        events.emit("test", "msg")
        self.assertEqual(sorted(results), ["h1:msg", "h2:msg"])

    def test_unsubscribe(self):
        events = EventSystem()
        results = []

        def handler(data):
            results.append(data)

        events.subscribe("test", handler)
        events.emit("test", "msg1")
        events.unsubscribe("test", handler)
        events.emit("test", "msg2")
        self.assertEqual(results, ["msg1"])

    def test_multiple_events(self):
        events = EventSystem()
        results = []

        def handler1(data):
            results.append(f"event1:{data}")

        def handler2(data):
            results.append(f"event2:{data}")

        events.subscribe("event1", handler1)
        events.subscribe("event2", handler2)
        events.emit("event1", "A")
        events.emit("event2", "B")
        self.assertEqual(results, ["event1:A", "event2:B"])

    def test_emit_nonexistent_event(self):
        events = EventSystem()
        events.emit("nonexistent", "data")


if __name__ == "__main__":
    unittest.main(verbosity=2)
