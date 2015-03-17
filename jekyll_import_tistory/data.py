# coding=utf-8
__author__ = 'rino0601'

import os
import codecs
import re
from datetime import datetime

import html2text

import yaml
from bs4 import BeautifulSoup


class Post(object):
    def __init__(self, is_draft, filename, yaml_header, content, downloads):
        self.is_draft = is_draft
        self.filename = filename
        self.yaml_header = yaml_header
        self.content = content
        self.downloads = downloads

    def write(self, jekyll_dir):
        output_dir = os.path.join(jekyll_dir, '_drafts' if self.is_draft else '_posts')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        file_path = os.path.join(output_dir, self.filename)

        with open(file_path, "w") as md_out:
            md_out.write("---\n")
            md_out.write(yaml.dump(self.yaml_header, default_flow_style=False, allow_unicode=True))
            md_out.write("---\n")

        with codecs.open(file_path, "a", encoding="utf-8") as md_out:
            md_out.write(self.content)


class PostBuilder(object):
    user_name = None
    dir_path = 'from_tistory'

    @classmethod
    def init_cls(cls, user_name, dir_path=dir_path):
        cls.user_name = user_name
        cls.dir_path = dir_path

    def __init__(self, soup_post):
        super(PostBuilder, self).__init__()
        self._text_id = soup_post.id.text
        self._text_visibility = soup_post.visibility.text
        self._text_title_unprocessed = soup_post.title.text
        self._html_content = soup_post.content.text
        self._text_date_num = soup_post.published.text
        self._file_data_to_download = []

    def _handle_tistory_attachment(self, html_content):
        pattern = re.compile(r'\[##_(?!Movie).*?\|(?P<pre_path>cfile.*?\.uf).(?P<post_path>.+?)\|(?P<attr>.*?)\|_##\]',
                             re.UNICODE)
        return pattern.sub(self._processing_attachment, html_content)

    def _processing_attachment(self, matched):
        file_path = matched.group('post_path')
        download_url = 'http://{tistory_url}/attachment/{pre_path}@{post_path}'.format(
            tistory_url='{user_name}.tistory.com'.format(user_name=self.user_name),
            pre_path=matched.group('pre_path'),
            post_path=file_path)
        dir_path = self.dir_path
        download_path = '{dir_path}/{file_path}'.format(
            dir_path=dir_path,
            file_path=file_path
        )
        self._file_data_to_download.append((download_url, dir_path, file_path))
        if 'image/jpeg' in matched.group('attr'):
            return u'<img src="{site_url_tmpl}{download_path}" {attr}>'.format(
                site_url_tmpl='{{site.url}}/',
                download_path=download_path,
                attr=matched.group('attr'))
        else:
            tag = u'<a href="{site_url_tmpl}{download_path}" {attr}></a>'.format(
                site_url_tmpl='{{site.url}}/',
                download_path=download_path,
                attr=matched.group('attr'))
            soup = BeautifulSoup(tag).a
            soup.string = soup['filename']
            return unicode(soup)

    def _handle_folded_content(self, html_content):
        pattern = re.compile(r'\[#M_(?P<open_span>.+?)\|(?P<close_span>.+?)\|(?P<content>.+?)_M#\]',
                             re.UNICODE)
        return pattern.sub(self._processing_folded_content, html_content)

    @staticmethod
    def _processing_folded_content(matched):
        return u'<div class="tistory_folded_content">' \
               u'<span class="open">{open_span}</span>' \
               u'<span class="close">{close_span}</span>' \
               u'{content}' \
               u'</div>'.format(open_span=matched.group('open_span'),
                                close_span=matched.group('close_span'),
                                content=matched.group('content'))

    def build(self, layout='post'):
        is_draft = self._text_visibility is 'public'
        filename = u'{timestamp}tistory-{id}.markdown'.format(
            id=self._text_id,
            timestamp=u'' if is_draft else datetime.fromtimestamp(int(self._text_date_num)).strftime('%Y-%m-%d-'))
        yaml_header = {
            'layout': layout,
            'title': u"%s" % self._text_title_unprocessed,
        }
        content = self._handle_tistory_attachment(self._html_content)
        content = self._handle_folded_content(content)
        content = html2text.html2text(content)
        return Post(is_draft, filename, yaml_header, content, self._file_data_to_download)