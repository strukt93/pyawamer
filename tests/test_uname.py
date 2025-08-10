import unittest
import os
from src.awamer import uname

class Testuname(unittest.TestCase):
    def test_uname_a(self):
        uname_cmd = uname.Uname().a()
        self.assertEqual(uname_cmd.run().out, os.popen('uname -a').read().strip())
    
    def test_uname_m(self):
        uname_cmd = uname.Uname().m()
        self.assertEqual(uname_cmd.run().out, os.popen('uname -m').read().strip())
    
    def test_uname_n(self):
        uname_cmd = uname.Uname().n()
        self.assertEqual(uname_cmd.run().out, os.popen('uname -n').read().strip())
    
    def test_uname_p(self):
        uname_cmd = uname.Uname().p()
        self.assertEqual(uname_cmd.run().out, os.popen('uname -p').read().strip())
    
    def test_uname_r(self):
        uname_cmd = uname.Uname().r()
        self.assertEqual(uname_cmd.run().out, os.popen('uname -r').read().strip())
    
    def test_uname_s(self):
        uname_cmd = uname.Uname().s()
        self.assertEqual(uname_cmd.run().out, os.popen('uname -s').read().strip())

    def test_uname_v(self):
        uname_cmd = uname.Uname().v()
        self.assertEqual(uname_cmd.run().out, os.popen('uname -v').read().strip())
    
    def test_uname_rms(self):
        uname_cmd = uname.Uname().r().m().s()
        self.assertEqual(uname_cmd.run().out, os.popen('uname -rms').read().strip())

if __name__ == '__main__':
    unittest.main()