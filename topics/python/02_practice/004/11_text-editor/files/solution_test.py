import unittest
from solution import TextEditor


class TestTextEditor(unittest.TestCase):
    def test_write(self):
        editor = TextEditor()
        editor.write("hello")
        self.assertEqual(editor.get_text(), "hello")

    def test_multiple_writes(self):
        editor = TextEditor()
        editor.write("hello")
        editor.write(" world")
        self.assertEqual(editor.get_text(), "hello world")

    def test_delete(self):
        editor = TextEditor()
        editor.write("hello world")
        editor.delete(6)
        self.assertEqual(editor.get_text(), "hello")

    def test_undo_write(self):
        editor = TextEditor()
        editor.write("hello")
        editor.write(" world")
        editor.undo()
        self.assertEqual(editor.get_text(), "hello")

    def test_undo_delete(self):
        editor = TextEditor()
        editor.write("hello world")
        editor.delete(6)
        editor.undo()
        self.assertEqual(editor.get_text(), "hello world")

    def test_redo(self):
        editor = TextEditor()
        editor.write("hello")
        editor.write(" world")
        editor.undo()
        editor.redo()
        self.assertEqual(editor.get_text(), "hello world")

    def test_complex_scenario(self):
        editor = TextEditor()
        editor.write("abc")
        editor.write("def")
        editor.delete(2)
        editor.undo()
        editor.undo()
        editor.redo()
        self.assertEqual(editor.get_text(), "abcdef")


if __name__ == "__main__":
    unittest.main(verbosity=2)
