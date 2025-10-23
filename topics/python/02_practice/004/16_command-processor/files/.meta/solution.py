class CommandProcessor:
    def __init__(self):
        self.commands = {}
        self.history = []

    def register_command(self, name, execute_fn, undo_fn):
        self.commands[name] = {
            "execute": execute_fn,
            "undo": undo_fn
        }

    def execute(self, name, *args):
        if name in self.commands:
            self.commands[name]["execute"](*args)
            self.history.append((name, args))

    def undo(self):
        if self.history:
            name, args = self.history.pop()
            self.commands[name]["undo"](*args)

    def get_history(self):
        return [name for name, args in self.history]
