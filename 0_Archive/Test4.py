#!/bin/env python3

import os.path
import subprocess
import sys

from ebooklib import epub

# This is just a basic example which can easily break in real world.

if __name__ == '__main__':
    # read epub
    book = epub.read_epub('stendhal_-_le_rouge_et_le_noir.epub')

    # get base filename from the epub
    base_name = 'stendhal_-_le_rouge_et_le_noir.epub'

    for item in book.items:
        # convert into markdown if this is html
        if isinstance(item, epub.EpubHtml):
            proc = subprocess.Popen(['pandoc', '-f', 'html', '-t', 'markdown', '-'],
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE)
            content, error = proc.communicate(item.content)
            file_name = os.path.splitext(item.file_name)[0] + '.md'
        else:
            file_name = item.file_name
            content = item.content

        # create needed directories 
        dir_name = '{0}/{1}'.format(base_name, os.path.dirname(file_name))
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        print('>> {0}'.format(file_name))

        # write content to file
        with open('{0}/{1}'.format(base_name, file_name), 'w') as f:
            f.write(content)
