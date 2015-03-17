# helped from http://www.scotttorborg.com/python-packaging/minimal.html

# might help http://click.pocoo.org/3/

__author__ = 'lemonApple'

from setuptools import setup

setup(name='jekyll_import_tistory',
      version='0.0.1',
      description='produce jekyll post from tistory backup.xml',
      url='http://github.com/rino0601/jekyll_import_tistory',
      author='rino0601',
      author_email='rino0601.dev@gmail.com',
      install_requires=['beautifulsoup4', 'PyYAML', 'Click', 'html2text', 'requests'],
      license='MIT',
      packages=['jekyll_import_tistory'],
      test_suite='jekyll_import_tistory',
      entry_points={
          'console_scripts': [
              'tistory2jekyll = jekyll_import_tistory.main:cli',
          ], },
      zip_safe=False)