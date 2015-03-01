# helped from http://www.scotttorborg.com/python-packaging/minimal.html

__author__ = 'lemonApple'

from setuptools import setup

setup(name='jekyll_import_tistory',
      version='0.1',
      description='produce jekyll post from tistory backup.xml',
      url='http://github.com/rino0601/jekyll_import_tistory',
      author='rino0601',
      author_email='rino0601@naver.com',
      license='MIT',
      packages=['jekyll_import_tistory'],
      zip_safe=False)