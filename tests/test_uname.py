import unittest
import os
from src.awamer import uname

class Testuname(unittest.TestCase):
    def test_uname_a(self):
        self.assertEqual(uname.uname(True), os.popen('uname -a').read().strip())
    
    def test_uname_m(self):
        self.assertEqual(uname.uname(False, True), os.popen('uname -m').read().strip())
    
    def test_uname_n(self):
        self.assertEqual(uname.uname(False, False, True), os.popen('uname -n').read().strip())
    
    def test_uname_p(self):
        self.assertEqual(uname.uname(False, False, False, True), os.popen('uname -p').read().strip())
    
    def test_uname_r(self):
        self.assertEqual(uname.uname(False, False, False, False, True), os.popen('uname -r').read().strip())
    
    def test_uname_s(self):
        self.assertEqual(uname.uname(False, False, False, False, False, True), os.popen('uname -s').read().strip())

    def test_uname_v(self):
        self.assertEqual(uname.uname(False, False, False, False, False, False, True), os.popen('uname -v').read().strip())
    
    def test_uname_rms(self):
        self.assertEqual(uname.uname(False, True, False, False, True, True), os.popen('uname -rms').read().strip())

if __name__ == '__main__':
    unittest.main()