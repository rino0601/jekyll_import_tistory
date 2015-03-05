__author__ = 'lemonApple'

import unittest
import os

from jekyll_import_tistory import main


class MyTestCase(unittest.TestCase):
    def test_can_open(self):
        something = main.main(open('../tistory-small.xml'))

        directory = '_drafts'
        if not os.path.exists(directory):
            os.makedirs(directory)

        for some in something:
            # some.write_to_md(directory)
            if some.find_tistory_meta():
                print some.text_id
                for s in some.find_tistory_meta().groups():
                    print s

        self.assertEqual(False, something)


if __name__ == '__main__':
    unittest.main()
