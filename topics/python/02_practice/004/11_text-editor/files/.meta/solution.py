class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def write(self, text):
        self.undo_stack.append(self.text)
        self.text += text
        self.redo_stack = []

    def delete(self, n):
        self.undo_stack.append(self.text)
        self.text = self.text[:-n] if n <= len(self.text) else ""
        self.redo_stack = []

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()

    def get_text(self):
        return self.text
