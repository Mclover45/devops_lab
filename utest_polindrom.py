import polindrom
import unittest


class test_polindrom(unittest.TestCase):

    def test_polindrom(self):
        self.assertFalse(polindrom.polin("zooooooosdfsdfooz"))
        self.assertTrue(polindrom.polin("zoooooooooz"))


if __name__ == '__main__':
    unittest.main()
