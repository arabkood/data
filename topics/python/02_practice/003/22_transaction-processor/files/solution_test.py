import unittest
from solution import processTransactions


class TestProcessTransactions(unittest.TestCase):
    def test_deposit_and_transfer(self):
        result = processTransactions([
            {"from": None, "to": "A", "amount": 100},
            {"from": "A", "to": "B", "amount": 50}
        ])
        self.assertEqual(result, {"A": 50, "B": 50})

    def test_deposit_and_withdrawal(self):
        result = processTransactions([
            {"from": None, "to": "A", "amount": 100},
            {"from": "A", "to": None, "amount": 30}
        ])
        self.assertEqual(result, {"A": 70})

    def test_multiple_accounts(self):
        result = processTransactions([
            {"from": None, "to": "A", "amount": 100},
            {"from": None, "to": "B", "amount": 50},
            {"from": "A", "to": "B", "amount": 25}
        ])
        self.assertEqual(result, {"A": 75, "B": 75})

    def test_empty_transactions(self):
        self.assertEqual(processTransactions([]), {})

    def test_single_deposit(self):
        result = processTransactions([{"from": None, "to": "A", "amount": 100}])
        self.assertEqual(result, {"A": 100})


if __name__ == "__main__":
    unittest.main(verbosity=2)
