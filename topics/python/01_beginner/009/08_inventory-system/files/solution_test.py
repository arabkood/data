import unittest
import subprocess
import sys
import os
import re


class TestInventorySystem(unittest.TestCase):
    """Test suite for Inventory System Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self):
        """Run the solution and return the output."""
        try:
            result = subprocess.run(
                [sys.executable, "solution.py"],
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

    def test_product_count(self):
        """Test: Shows correct number of products"""
        output = self.run_solution()

        # Check for product count
        self.assertIn(
            "عدد المنتجات: 2",
            output,
            "Missing or incorrect product count. Expected: 'عدد المنتجات: 2'",
        )

    def test_total_value_calculation(self):
        """Test: Calculates total inventory value correctly"""
        output = self.run_solution()

        # Look for total value line
        total_pattern = r"القيمة الإجمالية:\s*(\d+\.?\d*)"
        match = re.search(total_pattern, output)

        self.assertIsNotNone(
            match,
            "Missing total value line. Expected format: 'القيمة الإجمالية: <number>'",
        )

        # The total should be a reasonable number (not 0)
        total_value = float(match.group(1))
        self.assertGreater(total_value, 0, "Total value should be greater than 0")

    def test_low_stock_items(self):
        """Test: Shows low stock items header"""
        output = self.run_solution()

        self.assertIn(
            "المنتجات القليلة:",
            output,
            "Missing low stock items header: 'المنتجات القليلة:'",
        )

    def test_structure_has_list(self):
        """Test: Code contains list structure"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        # Check for list creation
        self.assertTrue(
            "inventory" in code and "[" in code,
            "Code should create a list named 'inventory'",
        )

    def test_structure_has_loop(self):
        """Test: Code contains for loop"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        self.assertIn("for", code, "Code should use a for loop to process inventory")

    def test_output_format(self):
        """Test: Output contains all required sections"""
        output = self.run_solution()

        # All three sections should be present
        required_parts = ["عدد المنتجات:", "القيمة الإجمالية:", "المنتجات القليلة:"]

        for part in required_parts:
            self.assertIn(part, output, f"Missing required output section: '{part}'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
