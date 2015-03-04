# coding=utf-8
__author__ = 'lemonApple'

import os
import codecs

from bs4 import BeautifulSoup


class Post(object):
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

    def __init__(self, title, date, category, filename, tags, content):
        super(Post, self).__init__()
        self.content = content
        self.tags = tags
        self.filename = filename
        self.category = category
        self.date = date
        self.title = title

    def write_to_md(self, output_dir):
        with codecs.open(os.path.join(output_dir, "%s-%s.markdown" % (self.date, self.filename)), "w",
                         encoding="utf-8") as f:
            f.write("---\n")
            f.write("layout: post\n")
            f.write("title: %s\n" % self.title)
            f.write("---\n")
            f.write(self.content)


def main(xml_file=None):
    soup = BeautifulSoup(xml_file)
    blog = soup.blog
    xml_posts = blog.find_all('post')
    posts = [Post(title=post.title.text, date=post.published.text, category=post.category.text, filename=post.id.text,
                  tags=post.find_all('tag'), content=post.content.text)
             for post in xml_posts]

    return posts[0]


if __name__ == '__main__':
    main()
