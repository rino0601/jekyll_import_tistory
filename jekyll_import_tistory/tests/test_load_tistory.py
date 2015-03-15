__author__ = 'lemonApple'

import unittest
import os

from jekyll_import_tistory import main


class MyTestCase(unittest.TestCase):
    def setUp(self):
        xml_path = os.path.join(os.path.dirname(__file__), os.pardir, 'tistory-small.xml')

        self.test_data = main.main(open(xml_path))
        self.drafts_dir_path = os.path.join(os.path.dirname(__file__), '_drafts')
        if not os.path.exists(self.drafts_dir_path):
            os.makedirs(self.drafts_dir_path)

    def test_re(self):
        for post_builder in self.test_data:
            if post_builder.temp_find_tistory_meta():
                print post_builder.text_id
                for s in post_builder.temp_find_tistory_meta().groups():
                    print s

        self.assertEqual(False, self.test_data)

    @unittest.skip("make test_re works first")
    def test_write_post(self):
        for post_builder in self.test_data:
            post_builder.temp_write_to_md(self.drafts_dir_path)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
