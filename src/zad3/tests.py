import unittest
from zad3 import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.temp = Song()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp
        
    def tearDown(self):
        self.temp = None 

if __name__ == '__main__':
    unittest.main()