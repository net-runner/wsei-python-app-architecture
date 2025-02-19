import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        account = BankAccount(100.0)
        self.assertEqual(account.get_balance(), 100.0)
        
        with self.assertRaises(ValueError):
            BankAccount(-50.0)
    
    def test_deposit(self):
        account = BankAccount(50.0)
        account.deposit(50.0)
        self.assertEqual(account.get_balance(), 100.0)
        
        with self.assertRaises(ValueError):
            account.deposit(-10.0)
        
        with self.assertRaises(ValueError):
            account.deposit(0)
    
    def test_withdraw(self):
        account = BankAccount(100.0)
        account.withdraw(50.0)
        self.assertEqual(account.get_balance(), 50.0)
        
        with self.assertRaises(ValueError):
            account.withdraw(-10.0)
        
        with self.assertRaises(ValueError):
            account.withdraw(0)
        
        with self.assertRaises(ValueError):
            account.withdraw(200.0)
    
    def test_insufficient_funds(self):
        account = BankAccount(30.0)
        with self.assertRaises(ValueError):
            account.withdraw(50.0)

if __name__ == "__main__":
    unittest.main()
