#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Publish a post

usage:
    ./publish.py -md <markdown_filename>
    ./publish.py -html <html_filename>
"""

import sys
import os
import codecs

import markdown
import post

def publish_markdown(filename):
    """Publish a Markdown-format post
    """
    # suppose post `title` is just `filename` without prefix-dirpath and suffix-extension
    title = os.path.splitext(os.path.basename(filename))[0]
    # suppose markdown-file and images are in the same folder
    img_base_path = os.path.dirname(filename)

    markdown_file = codecs.open(filename, 'r', encoding='utf-8')
    text = markdown_file.read()
    description = markdown.markdown(text, extensions=['extra', 'toc'])

    # wrapping `description` in div#markdown is just my favor, it's not necessary
    description = '<div id="markdown">\n\n%s\n\n</div>' % description

    post.new(title, description, img_base_path)

def publish_html(filename):
    """Publish a HTML-format post
    """
    html_file = codecs.open(filename, 'r', encoding='utf-8')
    content = html_file.read()

    title, description = post.parse_html(content)
    post.new(title, description)

# test
if __name__ == '__main__':
    if not (len(sys.argv) == 3 and sys.argv[1] in ('-md', '-html')):
        sys.stderr.write(__doc__)
        sys.exit(1)

    filename = os.path.abspath(sys.argv[2])
    try:
        if sys.argv[1] == '-md':
            publish_markdown(filename)
        else: # '-html'
            publish_html(filename)
    except Exception, e:
        print('failed\n\n%s' % str(e))
    else:
        print('succeeded')
