from collections import defaultdict


class EventSystem:
    def __init__(self):
        self.events = defaultdict(list)

    def subscribe(self, event, callback):
        self.events[event].append(callback)

    def unsubscribe(self, event, callback):
        if event in self.events and callback in self.events[event]:
            self.events[event].remove(callback)

    def emit(self, event, data):
        if event in self.events:
            for callback in self.events[event]:
                callback(data)
