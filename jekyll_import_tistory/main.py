# coding=utf-8
import os
import requests

__author__ = 'rino0601'

import click
from bs4 import BeautifulSoup

from jekyll_import_tistory import data


@click.command()
@click.argument('tistory_backup_min', type=click.File('r'))
@click.argument('your_jekyll_dir',
                type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, resolve_path=True))
def cli(tistory_backup_min, your_jekyll_dir):
    """
    This command make _post & _drafts directory from your tistory_backup.xml file.
    """
    click.echo(u"Welcome, Before we start converting, There is some things you have to know.")
    click.echo(u"   1. This tool does not support videos which you upload tistory directly.\n"
               u"   They seems only play able on tistory blog.\n"
               u"   If you have good idea for this, please contribute this project.\n"
               u"   2. This tool ignore comments, track backs, tags and categories. \n"
               u"   There is some different with jekyll and tistory's system.\n"
               u"   I didn't have enough time for consider that.\n"
               u"   3. If you want bring your picture and attachment from tistory, that blog has to be alive.\n"
               u"   (backup_with_attachment.xml isn't available for now.)\n")
    click.confirm(u'Do you want to continue?', abort=True)
    soup = BeautifulSoup(tistory_backup_min)
    user_id = soup.setting.find('name').string
    data.PostBuilder.init_cls(user_id)
    posts = [data.PostBuilder(post).build() for post in soup.blog.find_all('post')]
    with click.progressbar(posts, label=u"Converting posts...") as bar:
        for post in bar:
            post.write(your_jekyll_dir)

            # download attachments...
            for url, dir_path, file_path in post.downloads:
                save_dir = os.path.join(your_jekyll_dir, dir_path)
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                with open(os.path.join(save_dir, file_path), 'wb') as out:
                    response = requests.get(url, stream=True)
                    if not response.ok:
                        click.echo(u"[WARN]Couldn't access to {}".format(url))
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        out.write(block)
    click.echo(u"Done.")
