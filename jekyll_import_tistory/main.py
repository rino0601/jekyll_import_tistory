# coding=utf-8
__author__ = 'lemonApple'

from bs4 import BeautifulSoup

import data


def main(xml_file=None):
    soup = BeautifulSoup(xml_file)
    soup_blog = soup.blog
    soup_posts = soup_blog.find_all('post')
    posts = [data.PostBuilder(soup_post) for soup_post in soup_posts]

    return posts


if __name__ == '__main__':
    main()
