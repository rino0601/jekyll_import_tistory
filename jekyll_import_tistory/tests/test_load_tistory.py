__author__ = 'lemonApple'

import unittest

from jekyll_import_tistory import main


class MyTestCase(unittest.TestCase):
    def test_can_open(self):
        something = main.main(open('../tistory-small.xml'))
        self.assertEqual(False, something)


if __name__ == '__main__':
    unittest.main()
