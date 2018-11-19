import unittest
import polindrom
import coverage

class test_polindrom(unittest.TestCase):
    def setUp(self):

        """Init"""

    def test_polindrom(self):

        self.assertFalse(polindrom.polin("zooooooosdfsdfooz"))
        self.assertTrue(polindrom.polin("zoooooooooz"))

    def tearDown(self):

        """Finish"""
if __name__ == '__main__':
    unittest.main()