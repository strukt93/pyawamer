import unittest
import os
from src.awamer import pwd

class Testpwd(unittest.TestCase):
    def test_pwd(self):
        self.assertEqual(pwd.Pwd().run().out, os.popen('pwd').read().strip())

if __name__ == '__main__':
    unittest.main()