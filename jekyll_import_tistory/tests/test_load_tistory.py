__author__ = 'lemonApple'

import unittest
import os

from jekyll_import_tistory import main


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_data = main.main(open('../tistory-small.xml'))
        self.drafts_dir = '_drafts'
        if not os.path.exists(self.drafts_dir):
            os.makedirs(self.drafts_dir)

    def test_re(self):
        for post_builder in self.test_data:
            # post_builder.write_to_md(directory)
            if post_builder.temp_find_tistory_meta():
                print post_builder.text_id
                for s in post_builder.temp_find_tistory_meta().groups():
                    print s

        self.assertEqual(False, self.test_data)

    def test_write_post(self):
        for post_builder in self.test_data:
            post_builder.temp_write_to_md(self.drafts_dir)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
