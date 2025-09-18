import unittest
import subprocess
import sys
import os
import re


class TestMultiplicationTable(unittest.TestCase):
    """Test suite for the Multiplication Table Builder Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self, table_size):
        """Run the solution with given input and return the output."""
        input_data = str(table_size)

        try:
            result = subprocess.run(
                [sys.executable, "solution.py"],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=5,
                encoding="utf-8",
            )

            if result.returncode != 0:
                self.fail(f"Program crashed with error:\n{result.stderr}")

            return result.stdout

        except subprocess.TimeoutExpired:
            self.fail("Program took too long to run (possible infinite loop)")

    def extract_table_rows(self, output):
        """Extract the table rows from the output."""
        lines = output.strip().split("\n")
        table_rows = []

        # Skip prompt and title lines, extract only numeric rows
        for line in lines:
            # Check if line contains only numbers and spaces
            if re.match(r"^[\s\d]+$", line) and line.strip():
                # Extract all numbers from the line
                numbers = [int(x) for x in line.split()]
                if numbers:  # Only add non-empty rows
                    table_rows.append(numbers)

        return table_rows

    def verify_multiplication_table(self, output, size, test_name):
        """Verify the multiplication table is correct."""

        # Check for required prompt
        prompt = "أدخل حجم جدول الضرب"
        self.assertIn(
            prompt, output, f"Missing input prompt in test '{test_name}': '{prompt}'"
        )

        # Check for table title
        title_pattern = f"جدول الضرب {size}×{size}"
        self.assertIn(
            title_pattern,
            output,
            f"Missing or incorrect table title in test '{test_name}'",
        )

        # Extract and verify table rows
        table_rows = self.extract_table_rows(output)

        # Check correct number of rows
        self.assertEqual(
            len(table_rows),
            size,
            f"Test '{test_name}': Expected {size} rows, got {len(table_rows)}",
        )

        # Verify each row
        for i, row in enumerate(table_rows, 1):
            # Check correct number of columns
            self.assertEqual(
                len(row),
                size,
                f"Test '{test_name}': Row {i} should have {size} columns, got {len(row)}",
            )

            # Check multiplication values
            for j, value in enumerate(row, 1):
                expected = i * j
                self.assertEqual(
                    value,
                    expected,
                    f"Test '{test_name}': Position [{i}][{j}] should be {expected}, got {value}",
                )

        # Check formatting (alignment)
        self.verify_alignment(output, size, test_name)

    def verify_alignment(self, output, size, test_name):
        """Verify that the table columns are properly aligned."""
        lines = output.strip().split("\n")
        table_lines = []

        # Extract only the table rows (lines with numbers)
        for line in lines:
            if re.match(r"^[\s\d]+$", line) and line.strip():
                table_lines.append(line)

        if not table_lines:
            self.fail(f"Test '{test_name}': No table rows found in output")

        # Check that numbers are reasonably aligned
        # We'll be lenient - just check that each row has consistent spacing
        for i, line in enumerate(table_lines, 1):
            # Check minimum spacing between numbers
            if "  " not in line and size > 1:
                self.fail(
                    f"Test '{test_name}': Row {i} appears to have no spacing between numbers"
                )

    def test_small_table(self):
        """Test: 3×3 multiplication table"""
        output = self.run_solution(3)
        self.verify_multiplication_table(output, 3, "3×3 table")

    def test_medium_table(self):
        """Test: 5×5 multiplication table"""
        output = self.run_solution(5)
        self.verify_multiplication_table(output, 5, "5×5 table")

    def test_large_table(self):
        """Test: 10×10 multiplication table"""
        output = self.run_solution(10)
        self.verify_multiplication_table(output, 10, "10×10 table")

    def test_maximum_table(self):
        """Test: 12×12 multiplication table"""
        output = self.run_solution(12)
        self.verify_multiplication_table(output, 12, "12×12 table")

    def test_minimum_table(self):
        """Test: 1×1 multiplication table"""
        output = self.run_solution(1)
        self.verify_multiplication_table(output, 1, "1×1 table")

    def test_edge_case_alignment(self):
        """Test: Proper alignment with large numbers (12×12=144)"""
        output = self.run_solution(12)

        # Check that 144 is present and properly formatted
        self.assertIn(
            "144",
            output,
            "Test 'Large number alignment': Missing 144 (12×12) in output",
        )

        # Verify the table is still readable with 3-digit numbers
        lines = output.strip().split("\n")
        last_row = None
        for line in lines:
            if "144" in line:
                last_row = line
                break

        if last_row:
            # Check that the row with 144 is properly formatted
            numbers = re.findall(r"\d+", last_row)
            self.assertEqual(
                len(numbers), 12, "Last row of 12×12 table should have 12 numbers"
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
