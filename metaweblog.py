#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""MetaWeblog API Wrapper"""

import xmlrpclib
import os
import mimetypes
import logging

def handle(exc_res):
    """Return `exc_res` if exception occurs in func"""

    def wrapOuter(func):
        def wrapInner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception, e:
                logging.error(str(e))
                return exc_res
        return wrapInner

    return wrapOuter

class MetaWeblog:
    """MetaWeblog API Wrapper.

    Normal case:

        >>> from config import config
        >>> weblog = MetaWeblog(**config)
        >>> weblog.getPost('3338616').get('title')
        u'\u7528Python\u5199\u4e00\u4e2a\u7b80\u5355\u7684Web\u6846\u67b6'

    Exception case:

        >>> from config import config
        >>> config['passwd'] = 'wrong'
        >>> weblog = MetaWeblog(**config)
        >>> weblog.getPost('3338616')
        {}
    """

    def __init__(self, url, appKey, user, passwd):
        self.url, self.appKey, self.user, self.passwd = url, appKey, user, passwd
        self.proxy = xmlrpclib.ServerProxy(self.url)

    @handle('')
    def newPost(self, title, description, mt_keywords, publish, **kwargs):
        return self.proxy.metaWeblog.newPost('', self.user, self.passwd, 
                   dict(title=title, description=description, mt_keywords=mt_keywords, **kwargs), publish)

    @handle(False)
    def editPost(self, postid, title, description, mt_keywords, publish, **kwargs):
        return self.proxy.metaWeblog.editPost(postid, self.user, self.passwd, 
                   dict(title=title, description=description, mt_keywords=mt_keywords, **kwargs), publish)

    @handle(False)
    def deletePost(self, postid):
        return self.proxy.blogger.deletePost(self.appKey, postid, self.user, self.passwd, False)

    @handle({})
    def getPost(self, postid):
        return self.proxy.metaWeblog.getPost(postid, self.user, self.passwd)

    @handle([])
    def getRecentPosts(self, count):
        return self.proxy.metaWeblog.getRecentPosts('', self.user, self.passwd, count)

    @handle({})
    def newMediaObject(self, abspath):
        with open(abspath) as f:
            bits = xmlrpclib.Binary(f.read())
        type = mimetypes.guess_type(abspath)[0]
        name = os.path.basename(abspath)
        return self.server.metaWeblog.newMediaObject('', self.user, self.passwd, dict(bits=bits, name=name, type=type))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
