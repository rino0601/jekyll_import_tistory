# coding=utf-8
__author__ = 'lemonApple'

import os
import codecs
import re

import yaml
from bs4 import BeautifulSoup


class Post(object):
    def __init__(self, is_draft, filename, title, category, tags, content):
        self.is_draft = is_draft
        self.filename = filename
        self.title = title
        self.category = category
        self.tags = tags
        self.content = content


class PostBuilder(object):
    """
    sample
    ----
    <post slogan="좋은-페이지-목록" format="1.1">
        <author domain="tistory">717353</author>
        <id>2</id>
        <isKorea>Y</isKorea>
        <visibility>public</visibility>
        <title>좋은 페이지 목록</title>
        <content>&lt;p&gt;한 해동안 코딩하면서 참고했던 웹들을 가지고 있는 블로그 주소 입니다.&lt;/p&gt;&lt;p&gt;&lt;strike&gt;대충 분류 하자면&lt;/strike&gt;&amp;nbsp;너무
            많아서 나중에 천천히 분류하기로...&lt;/p&gt;&lt;p&gt;= 티스토리 =&lt;/p&gt;&lt;p&gt;http://cocoadev.tistory.com&lt;/p&gt;&lt;p&gt;http://iphoneappsmaker.tistory.com&lt;/p&gt;&lt;p&gt;http://pcraft.tistory.com&lt;/p&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;http://hansune.tistory.com&lt;/p&gt;&lt;p&gt;http://javastore.tistory.com&lt;/p&gt;&lt;p&gt;http://dudfufl.tistory.com&lt;/p&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;http://dongss.tistory.com&lt;/p&gt;&lt;p&gt;http://eioie.tistory.com&lt;/p&gt;&lt;p&gt;http://thlife.tistory.com&lt;/p&gt;&lt;p&gt;http://khmirage.tistory.com&lt;/p&gt;&lt;p&gt;http://alloc.tistory.com&lt;/p&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;http://fptf.tistory.com&lt;/p&gt;&lt;p&gt;&lt;br
            /&gt;&lt;/p&gt;&lt;p&gt;= 그 외&amp;nbsp;=&lt;/p&gt;&lt;p&gt;&lt;/p&gt;&lt;p&gt;http://yooninsung.blog.me&lt;/p&gt;&lt;p&gt;http://www.econovation.co.kr/Main.asp&lt;/p&gt;&lt;p&gt;http://telewar.springnote.com&lt;/p&gt;&lt;p&gt;http://blog.naver.com/yulian&lt;/p&gt;&lt;p&gt;http://soooprmx.com/wp/&lt;/p&gt;&lt;p&gt;http://www.iphonesdkarticles.com&lt;/p&gt;&lt;p&gt;http://sweeper.egloos.com&lt;/p&gt;&lt;p&gt;http://dvmn.egloos.com&lt;/p&gt;&lt;p&gt;http://happydeveloper.springnote.com&lt;/p&gt;&lt;p&gt;http://mongkoon.com/blog/&lt;/p&gt;&lt;p&gt;http://www.java2s.com&lt;/p&gt;&lt;p&gt;http://blog.naver.com/hisukdory&lt;/p&gt;&lt;p&gt;http://www.androidpub.com&lt;/p&gt;&lt;p&gt;http://iphoneappsmaker.tistory.com&lt;/p&gt;&lt;p&gt;http://icanelite.blogspot.kr&lt;/p&gt;&lt;p&gt;http://blog.naver.com/ghbn15&lt;/p&gt;&lt;p&gt;http://www.digipine.com/programming/&lt;/p&gt;&lt;p&gt;http://www.haandol.com&lt;/p&gt;&lt;p&gt;http://www.iphonedevsdk.com&lt;/p&gt;&lt;p&gt;http://www.stcocoa.com&lt;/p&gt;&lt;p&gt;http://maclove.pe.kr&lt;/p&gt;&lt;p&gt;&lt;br
            /&gt;&lt;/p&gt;&lt;p&gt;그냥 페이지만 가지고 왔는데 수가 꽤 되네요, 읽기목록에 있는 내용들 정리해서 올리기만 해도 꽤 많은 포스트가 나올 것 같습니다.&lt;/p&gt;&lt;p&gt;&lt;br
            /&gt;&lt;/p&gt;&lt;p&gt;&lt;br /&gt;&lt;/p&gt;</content>
        <location>/</location>
        <password>1otq2mjq</password>
        <acceptComment>1</acceptComment>
        <acceptTrackback>1</acceptTrackback>
        <published>1341748567</published>
        <created>1341748567</created>
        <modified>1341748581</modified>
        <device>2</device>
        <uselessMargin>0</uselessMargin>
        <category>잡담</category>
        <comment>
            <commenter id="717353">
                <name>레몬사과</name>
                <homepage>http://rino0601.tistory.com</homepage>
                <ip>165.194.35.75</ip>
            </commenter>
            <content>언제 다 정리하지 ㅇㅈㄴ....
                지금은 이게 더 늘어났음(...)
            </content>
            <password></password>
            <secret>0</secret>
            <written>1344563801</written>
            <isFiltered>0</isFiltered>
        </comment>
        <trackback>
            <url>http://www.colegiosam.com/bolsos/michael-kors-kempton-121.html</url>
            <site>michael kors kempton</site>
            <title>michael kors kempton</title>
            <excerpt>레몬 생으로 씹어먹으면 맛있어요. :: 좋은 페이지 목록</excerpt>
            <ip>176.31.105.91</ip>
            <received>1414650385</received>
            <isFiltered>0</isFiltered>
        </trackback>
        <trackback>
            <url>http://www.hayek-club-passau.de/page/</url>
            <site>billige nike air max 1</site>
            <title>billige nike air max 1</title>
            <excerpt>레몬 생으로 씹어먹으면 맛있어요. :: 좋은 페이지 목록</excerpt>
            <ip>192.99.6.68</ip>
            <received>1415626046</received>
            <isFiltered>0</isFiltered>
        </trackback>
    </post>
    """

    def __init__(self, soup_post):
        super(PostBuilder, self).__init__()
        self.soup_post = soup_post
        self.text_id = soup_post.id.text
        self.text_visibility = soup_post.visibility.text
        self.text_title_unprocessed = soup_post.title.text
        self.html_content = soup_post.content.text
        self.soup_tags = soup_post.find_all('tag')
        self.text_date_num = soup_post.published.text
        self.text_category = soup_post.category.text
        self.soup_comments = soup_post.find_all('comment')

    def build(self):
        pass

    def temp_write_to_md(self, output_dir):
        header_yaml = {
            'layout': 'post',  # FIXME: hardcoded
            'title': u"%s" % self.text_title_unprocessed,
        }
        file_path = os.path.join(output_dir, "%s-%s.markdown" % (self.text_date_num, self.text_id))  # FIXME: hardcoded

        with open(file_path, "w") as md_out:
            md_out.write("---\n")
            md_out.write(yaml.dump(header_yaml, default_flow_style=False, allow_unicode=True))
            md_out.write("---\n")

        self.html_content = handle_tistory_attachment(self.html_content)
        self.html_content = handle_folded_content(self.html_content)

        with codecs.open(file_path, "a", encoding="utf-8") as md_out:
            md_out.write(self.html_content)

    def temp_find_movie(self):
        pass


def handle_tistory_attachment(html_content):
    pattern = re.compile(r'\[##_(?!Movie).*?\|(?P<pre_path>cfile.*?\.uf).(?P<post_path>.+?)\|(?P<attr>.*?)\|_##\]',
                         re.UNICODE)
    return pattern.sub(_processing_attachment, html_content)


def _processing_attachment(matched):
    download_url = 'http://{tistory_url}/attachment/{pre_path}@{post_path}'.format(
        tistory_url='rino0601.tistory.com',  # FIXME: hardcoded
        pre_path=matched.group('pre_path'),
        post_path=matched.group('post_path'))
    print download_url
    download_path = '{dir_path}/{file_path}'.format(
        dir_path='from_tistory',  # FIXME: hardcoded
        file_path=matched.group('post_path')
    )
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


def handle_folded_content(html_content):
    pattern = re.compile(r'\[#M_(?P<open_span>.+?)\|(?P<close_span>.+?)\|(?P<content>.+?)_M#\]',
                         re.UNICODE)
    return pattern.sub(_processing_folded_content, html_content)


def _processing_folded_content(matched):
    return u'<div class="tistory_folded_content">' \
           u'<span class="open">{open_span}</span>' \
           u'<span class="close">{close_span}</span>' \
           u'{content}' \
           u'</div>'.format(open_span=matched.group('open_span'),
                            close_span=matched.group('close_span'),
                            content=matched.group('content'))