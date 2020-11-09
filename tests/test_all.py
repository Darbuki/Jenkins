import myadder.add
import unittest
class TestAll(unittest.TestCase):
    def testBasically(self):
        self.assertEqual(myadder.add.add(2,2),4)
            
