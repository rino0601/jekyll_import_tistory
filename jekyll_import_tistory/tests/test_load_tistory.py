# coding=utf-8
__author__ = 'rino0601'

import unittest
import os

from bs4 import BeautifulSoup

from jekyll_import_tistory import data


class MyTestCase(unittest.TestCase):
    def setUp(self):
        xml_path = os.path.join(os.path.dirname(__file__), os.pardir, 'backup-file-for-test.xml')
        with open(xml_path) as xml:
            soup = BeautifulSoup(xml)
            self.builder = data.PostBuilder(soup.blog.post)

    def test_folded_content(self):
        test_input = u'[#M_openCV 받기|접기|<p>우선 sorceForge.net으로 갑니다. </p>_M#]'
        expect_output = u'<div class="tistory_folded_content">' \
                        u'<span class="open">openCV 받기</span>' \
                        u'<span class="close">접기</span>' \
                        u'<p>우선 sorceForge.net으로 갑니다. </p>' \
                        u'</div>'
        actual = self.builder._handle_folded_content(test_input)
        self.assertMultiLineEqual(actual, expect_output)

    def test_attachment(self):
        test_inputs = [
            u'<p>[##_1C|cfile25.uf.1567DD4E5038E96E322C75.001|'
            u'filename="공강사수 프로그램.7z.001" filemime="application/x-7z-compressed"|_##]</p>',
            u'<p>[##_1C|cfile25.uf.116EED4E5038E97628E551.002|'
            u'filename="공강사수 프로그램.7z.002" filemime="application/octet-stream"|_##]</p>',
            u'<p>[##_1C|cfile27.uf.197FC64E5038E97E1693EF.003|'
            u'filename="공강사수 프로그램.7z.003" filemime="application/octet-stream"|_##]</p>',
            u'>[##_1C|cfile23.uf.1929B64850A651382796D3.PNG|'
            u'width="320" height="480" filename="Lena.PNG" filemime="image/jpeg"|_##]</p>',
            u'>[##_Movie|kE9NExnxXoE$|http://cfile5.uf.tistory.com/image/163D643A50A651F4388770_##]</p>',
        ]
        expected_outputs = [
            u'<p><a filemime="application/x-7z-compressed" filename="공강사수 프로그램.7z.001" '
            u'href="{{site.url}}/from_tistory/1567DD4E5038E96E322C75.001">공강사수 프로그램.7z.001</a></p>',
            u'<p><a filemime="application/octet-stream" filename="공강사수 프로그램.7z.002" '
            u'href="{{site.url}}/from_tistory/116EED4E5038E97628E551.002">공강사수 프로그램.7z.002</a></p>',
            u'<p><a filemime="application/octet-stream" filename="공강사수 프로그램.7z.003" '
            u'href="{{site.url}}/from_tistory/197FC64E5038E97E1693EF.003">공강사수 프로그램.7z.003</a></p>',
            u'><img src="{{site.url}}/from_tistory/1929B64850A651382796D3.PNG" '
            u'width="320" height="480" filename="Lena.PNG" filemime="image/jpeg"></p>',
            u'>[##_Movie|kE9NExnxXoE$|http://cfile5.uf.tistory.com/image/163D643A50A651F4388770_##]</p>'
        ]
        for test_input, expect in zip(test_inputs, expected_outputs):
            actual = self.builder._handle_tistory_attachment(test_input)
            self.assertMultiLineEqual(actual, expect)


if __name__ == '__main__':
    unittest.main()
